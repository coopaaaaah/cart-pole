import gym
env = gym.make('CartPole-v0')
for i_episode in range(5):
    observation = env.reset()
    for t in range(100):
        env.render()
        action = env.action_space.sample() # this is a random action
        observation, reward, done, info = env.step(action)
        print(observation)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
env.close()



'''
question: how can we improve the action so that it doesn't have to be random?

what does the game state look like? (what do we observe?)
"Box" - Vector of 4 numbers 
[ a, b, c, d ]

action - Discrete(2)
    0 - move left
    1 - move right

when is something considered "done" - is there a correlation between the observation and something being done

!! done's correlation to an observation is the failure range


'''
