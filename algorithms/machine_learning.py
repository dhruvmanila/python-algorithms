"""
Reinforcement Learning:

The Machine will be given a command and a number, it will return the value
after applying a random action (function) to it. After the command has
returned it will be given a response (True/False) if the response is true
then the action was done good, if the response is false then the action
was a bad one. This is a program where the machine will learn to apply an
action to a given command using the reponse given and learn from its mistakes
according to the feedback received.
"""
import random

ACTION_LIST = [
    lambda x: x + 1,
    lambda x: 0,
    lambda x: x / 2,
    lambda x: x * 100,
    lambda x: x % 2
]


def get_action_list():
    return ACTION_LIST[:]


class Machine:
    """Create a machine object which uses reinforcement learning."""
    def __init__(self):
        """
        Initialize machine attributes:
        Memory contains the command to action elements.
        Tried contains which actions tried w.r.t. the current command
        cmd is the current command
        act is the current action
        """
        self._action_list = get_action_list()
        self._cmd = None
        self._act = None
        self._memory = {}
        self._tried = {}

    def command(self, cmd, num):
        """
        If command is in the memory, return the result.
        Update the cmd and act value to the current command and action
        so that if it turned out to be incorrect we can add it to our
        tried list.
        Otherwise, start trying different actions, skipping the ones
        already tried.
        """
        self._cmd = cmd
        if cmd in self._memory:
            self._act = self._memory[cmd]
            return self._act(num)

        for action in self._action_list:
            if self._cmd not in self._tried:
                self._tried[self._cmd] = []
            if action in self._tried[self._cmd]:
                continue
            self._act = action
            return action(num)

    def response(self, feedback):
        """
        Update the memory and tried list according to the feedback.
        If command is in memory and later on it turned out to be
        incorrect, delete it and add that action to tried list.
        """
        if feedback and self._cmd not in self._memory:
            self._memory[self._cmd] = self._act
        elif not feedback:
            if self._cmd in self._memory:
                del self._memory[self._cmd]
            self._tried[self._cmd].append(self._act)


# --------------------- Test programs ---------------------
def test_machine():
    test_m1 = Machine()
    random.seed()

    # Training machine 1
    for _ in range(0, 20):
        m1_return = test_m1.command(0, random.randint(0, 100))
        test_m1.response(m1_return == 0)

    # Testing machine 1
    print("#1 Should apply the num * 0 action to the command 0")
    try:
        assert test_m1.command(0, random.randint(0, 100)) == 0
        print('Test PASSED\n')
    except AssertionError:
        print('Test FAILED\n')

    test_m2 = Machine()
    random.seed()
    tests = [
        (0, 100, 101, "#2 Should apply the num + 1 action to the command 0"),
        (1, 100, 0, "#3 Should apply the num * 0 action to the command 1"),
        (2, 100, 50, "#4 Should apply the num / 2 action to the command 2"),
        (3, 1, 100, "#5 Should apply the num * 100 action to the command 3"),
        (4, 100, 0, "#6 Should apply the num % 2 action to the command 4")
    ]

    # Training machine 2
    for i in range(0, 200):
        rand_num = random.randint(0, 100)
        m2_return = test_m2.command(i % 5, rand_num)
        test_m2.response(ACTION_LIST[i % 5](rand_num) == m2_return)

    # Testing machine 2
    for t in tests:
        test_return_2 = test_m2.command(t[0], t[1])
        print(t[3])
        try:
            assert test_return_2 == t[2]
            print('Test PASSED\n')
        except AssertionError:
            print('Test FAILED\n')

    print("Random tests")
    for a in range(0, 100):
        cmd = random.randint(0, 1000000)
        action_index = random.randint(0, 4)
        test_num = random.randint(0, 10000)
        t = (cmd, ACTION_LIST[action_index], test_num, action_index)

        test_machine_rand = Machine()

        # Training
        for i in range(0, 20):
            rand_num = random.randint(0, 100)
            machine_return = test_machine_rand.command(t[0], rand_num)
            test_machine_rand.response(machine_return == t[1](rand_num))

        # Testing
        output = test_machine_rand.command(t[0], t[2])
        expected = t[1](t[2])
        try:
            assert output == expected
            print(f"#{a + 1} PASSED | Expected: {expected} Output: {output} "
                  f"for cmd {t[0]} to action {t[3]} on {t[2]}")
        except AssertionError:
            print(f"#{a + 1} FAILED | Expected: {expected} Output: {output} "
                  f"for cmd {t[0]} to action {t[3]} on {t[2]}")


if __name__ == '__main__':
    test_machine()
