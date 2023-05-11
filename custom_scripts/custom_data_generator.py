from llama import LLM
from llama import Type, Context

position_parse_llm = LLM(name="position_parser")

class ParsedPosition(Type):
    object_name: str = Context("name of the object")
    object_count: str = Context("number of the object")
    object_description: str = Context("description of the object")
    object_relative_position: str = Context("relative position of the object to its parent")
    object_relative_distance: str = Context("relative distance of the object to its parent")
    object_parent: str = Context("parent of the object")

class PositionToParse(Type):
    position_description: str = Context("position to parse")

def get_position_data():
    return [
        [
          PositionToParse(position_description="A jumping boy is right to a car"),
          ParsedPosition(
            object_name="boy",
            object_count="1",
            object_description="lively jumping boy",
            object_relative_position="right",
            object_relative_distance="close",
            object_parent="car",
          ),
        ],
        [
          PositionToParse(position_description="a car is driving right to the house"),
          ParsedPosition(
            object_name="car",
            object_count="1",
            object_description="common red car",
            object_relative_position="right",
            object_relative_distance="near",
            object_parent="house",
          ),
        ],
        [
          PositionToParse(position_description="A windmill is in the middle of a green field"),
          ParsedPosition(
            object_name="windmill",
            object_count="1",
            object_description="village windmill",
            object_relative_position="middle",
            object_relative_distance="close",
            object_parent="field",
          ),
        ],
    ]

position_parse_llm.add_data(get_position_data())

def parse_position(position_description: str) -> ParsedPosition:
    return position_parse_llm(position_description, output_type=ParsedPosition, random=True)

example_position_parse = parse_position(position_description=PositionToParse(position_description="a duck is right to the boat"))

print(example_position_parse)