import numpy as np


time_steps = 100
input_features = 32
output_features = 64

def main():

    inputs = np.random.random((time_steps, input_features))

    state_t = np.zeros((output_features,))

    W = np.random.random((output_features, input_features))
    U = np.random.random((output_features, output_features))
    b = np.random.random((output_features,))

    last_out = []
    for input_ in inputs:
        output_t = np.tanh(np.dot(W, input_) + np.dot(U, state_t) + b)

        last_out.append(output_t)

        state_t = output_t
    final_output_sequence = np.stack(last_out, axis=0)
        





if __name__ == "__main__":
    main()