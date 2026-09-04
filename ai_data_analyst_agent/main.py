from agent import Agent


agent = Agent()


while True:

    user_query = input("\nYou: ")

    if user_query.lower() == "exit":
        break

    answer = agent.run(user_query)

    print("\nAgent:", answer)
