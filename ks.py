from typing import *
from pde import PDEBase, ScalarField, CartesianGrid, MemoryStorage, plot_kymograph


NX = 32 # number of cells in x
TMAX = 100 # time
DT = .01 # step
EPSILON = 1/2 # 1/2


class KS_PDE(PDEBase):
    """Implementation of the Kuramoto–Sivashinsky equation
    https://py-pde.readthedocs.io/en/latest/examples_gallery/pde_custom_class.html
    """
    def evolution_rate(self, u:ScalarField,
                       t:float = 0, eps:float = EPSILON) -> ScalarField:
        """implement the python version of the evolution equation"""
        u_xx = u.laplace(bc="auto_periodic_neumann")
        u_xxxx = u_xx.laplace(bc="auto_periodic_neumann")
        u_x_sq = u.gradient(bc="auto_periodic_neumann").to_scalar("squared_sum")
        return -eps * u_x_sq - u_xx - u_xxxx

    def simulate_1d(self,
                    nx:int = NX,
                    tmax:float = TMAX,
                    dt:float = DT,
                    state:ScalarField = None,
                    ) -> Union[ScalarField, MemoryStorage]:
        if not (isinstance(state, ScalarField) and state):
            grid = CartesianGrid([[0, NX]], [NX], periodic=True)
            state = ScalarField.random_uniform(grid)
        else:
            grid = state.grid
        self.last_sim = MemoryStorage()
        eq = PDE({"u": "-gradient_squared(u) / 2 - laplace(u + laplace(u))"})
        _evolve()
        final_state = self.solve(state, t_range = tmax,
                                 tracker = self.last_sim.tracker(dt))
        return final_state


if __name__ == '__main__':
    ks = KS_PDE()
    ks.simulate_1d()
    plot_kymograph(ks.last_sim)

