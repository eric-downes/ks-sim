from numpy import pi
from pde import PDE, ScalarField, CartesianGrid, MemoryStorage, plot_kymograph

NX = 100 # number of cells in x
TMAX = 220 # time
DT = .01 # step

def simulate_ks_1d(nx:int = NX,
                   tmax:float = TMAX,
                   dt:float = DT,
                   state:ScalarField = None,
                   ) -> MemoryStorage:
    if not (isinstance(state, ScalarField) and state):
        grid = CartesianGrid([[1, NX]], [NX], periodic=True)
        state = ScalarField.from_expression(grid, "sin(x)")
        #state = ScalarField.random_uniform(grid)
    else:
        grid = state.grid
    sim = MemoryStorage()
    eq = PDE({"u": "-gradient_squared(u) / 2 - laplace(u + laplace(u))"})
    eq.solve(state, t_range = tmax, dt = dt, tracker = sim.tracker(10 * dt))
    return sim


if __name__ == '__main__':
    sim = simulate_ks_1d()
    plot_kymograph(sim)

