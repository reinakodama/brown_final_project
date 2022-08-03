from typing import Callable

from adversarialsearchproblem import (
    Action,
    AdversarialSearchProblem,
    State as GameState,
)

# variable = float("inf") or float("-inf")
def mini(asp, state, player):
    if asp.is_terminal_state(state):
        return (asp.evaluate_terminal(state))[player]
    best_value = float("inf")
    possible_actions = asp.get_available_actions(state)
    for action in possible_actions:
        best_value = min(best_value, maxi(asp, (asp.transition(state, action)), player))
    return best_value

def maxi(asp, state, player):
    if asp.is_terminal_state(state):
        return asp.evaluate_terminal(state)[player]
    best_value = float("-inf")
    possible_actions = asp.get_available_actions(state)
    for action in possible_actions:
        best_value = max(best_value, mini(asp, (asp.transition(state, action)), player))
    return best_value


# check if there is an action left to see if all the squres are filled in
def minimax(asp: AdversarialSearchProblem[GameState, Action]) -> Action:
    start_state = asp.get_start_state()
    best_value = float("-inf")
    best_action = None
    player = start_state.player_to_move()
    for action in asp.get_available_actions(start_state):
        next_state = asp.transition(start_state, action)
        temp_value = mini(asp, next_state, player)
        if temp_value > best_value:
            best_value = temp_value
            best_action = action
    return best_action 

    #for loop?
    #what will the loop help determine
    #how would the output, output the action that needs to be taken(the best move possible)

    # goal state is true
    # output something
    # else run if statement
    # if counter is not divisible by 2
    # get availabe actions 
    # select maximum value
    # input value into transition function
    # set current_state to the output of the transition function
    # loop

    # what is the goal state?
    # how to determine max and min values out of the possible actions
    """
    Implement the minimax algorithm on ASPs, assuming that the given game is
    both 2-player and constant-sum.

    Input:
        asp - an AdversarialSearchProblem
    Output:
        an action (an element of asp.get_available_actions(asp.get_start_state()))
    """
    ...


def alpha_beta(asp: AdversarialSearchProblem[GameState, Action]) -> Action:

    my_stack = adversarialsearchproblem.Stack
    # while goal state is true
    # goal is four in a row or a filled board (draw)
    # output the output
    # else run if statement
    # if counter is not divisible by 2
    # maximizing player = -infinity
    # get the first available actions
    # select the maximizing
    # if counter is divisible by 2 
    # minimizing player = infinity
    # select maximum value
    # input value into transition function
    # set current_state to the output of the transition function
    # loop


    """
    Implement the alpha-beta pruning algorithm on ASPs,
    assuming that the given game is both 2-player and constant-sum.

    Input:
        asp - an AdversarialSearchProblem
    Output:
        an action(an element of asp.get_available_actions(asp.get_start_state()))
    """
    ...


def alpha_beta_cutoff(
    asp: AdversarialSearchProblem[GameState, Action],
    cutoff_ply: int,
    # See AdversarialSearchProblem:heuristic_func
    heuristic_func: Callable[[GameState], float],
) -> Action:
    """
    This function should:
    - search through the asp using alpha-beta pruning
    - cut off the search after cutoff_ply moves have been made.

    Input:
        asp - an AdversarialSearchProblem
        cutoff_ply - an Integer that determines when to cutoff the search and
            use heuristic_func. For example, when cutoff_ply = 1, use
            heuristic_func to evaluate states that result from your first move.
            When cutoff_ply = 2, use heuristic_func to evaluate states that
            result from your opponent's first move. When cutoff_ply = 3 use
            heuristic_func to evaluate the states that result from your second
            move. You may assume that cutoff_ply > 0.
        heuristic_func - a function that takes in a GameState and outputs a
            real number indicating how good that state is for the player who is
            using alpha_beta_cutoff to choose their action. You do not need to
            implement this function, as it should be provided by whomever is
            calling alpha_beta_cutoff, however you are welcome to write
            evaluation functions to test your implemention. The heuristic_func
            we provide does not handle terminal states, so evaluate terminal
            states the same way you evaluated them in the previous algorithms.
    Output:
        an action(an element of asp.get_available_actions(asp.get_start_state()))
    """
    ...
