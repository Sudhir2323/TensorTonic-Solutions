Random generation for neural network initialization for weights 





rng=np.random.default_rng(seed=42)

this tells me thhat we are making a generator with a seed values for reporiucibility

rng.random((3, 4))           # uniform [0, 1), shape (3, 4)

rng.uniform(low=2, high=5, size=(3, 4))  # uniform [2, 5)