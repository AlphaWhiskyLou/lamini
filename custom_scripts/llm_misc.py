from llama import Type, Context, LLM

class Animal(Type):
    name: str = Context("name of the animal")
    n_legs: int = Context("number of legs that animal has")

class Speed(Type):
    speed: float = Context("how fast something can run")

class Story(Type):
    story: str = Context("Story of an animal")


llama_animal = Animal(name="Larry", n_legs=4)
centipede_animal = Animal(name="Cici", n_legs=100)

my_data = [llama_animal, centipede_animal]

dog_animal = Animal(name="Nacho", n_legs=4)
dog_speed = Story(story="There once was a cute doggo named Nacho. She was a golden retriever who liked to run. All four of her paws were adorable.")

my_data.append([dog_animal, dog_speed])

llm = LLM(name="animal_stories")

llm.add_data(my_data)
llm.improve(on="story", to="specify the number of legs in a subtle way")

story = llm(llama_animal, output_type=Story)

print(story.story)
