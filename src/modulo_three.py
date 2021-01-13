from automata.fa.dfa import DFA


def main():
    modulo = DFA(
        states={"q0", "q1", "q2"},
        input_symbols={"0", "1"},
        transitions={
            "q0": {"0": "q0", "1": "q1"},
            "q1": {"0": "q2", "1": "q0"},
            "q2": {"0": "q1", "1": "q2"},
        },
        initial_state="q0",
        final_states={"q0"},
    )
    for i in modulo.read_input_stepwise("110"):
        print(i)


if __name__ == "__main__":
    main()
