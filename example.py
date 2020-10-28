import nengo
import nengo_dl

with nengo.Network() as net:
a = nengo.Node(output=[1])
b = nengo.Ensemble(n_neurons=100, dimensions=1)
nengo.Connection(a, b)
p = nengo.Probe(b)

with nengo_dl.Simulator(net) as sim:
sim.run(1.0)
print(sim.data[p])