import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

class SemaphoreSystem:
    def __init__(self) -> None:
        self.V1 = ctrl.Antecedent(np.arange(0, 51, 1), 'V1')
        self.V2 = ctrl.Antecedent(np.arange(0, 61, 1), 'V2')
        self.T = ctrl.Consequent(np.arange(10, 61, 1), 'T')

        self.define_members()

        self.control_system = ctrl.ControlSystem(self.rules())
        self.simulator = ctrl.ControlSystemSimulation(self.control_system)

    def define_members(self) -> None:
        self.V1['few'] = fuzz.trapmf(self.V1.universe, [0, 0, 10, 20])
        self.V1['moderate'] = fuzz.trimf(self.V1.universe, [10, 25, 40])
        self.V1['many'] = fuzz.trapmf(self.V1.universe, [30, 40, 50, 50])

        self.V2['few'] = fuzz.trapmf(self.V2.universe, [0, 0, 15, 30])
        self.V2['moderate'] = fuzz.trapmf(self.V2.universe, [0, 30, 45, 50])
        self.V2['many'] = fuzz.trapmf(self.V2.universe, [35, 45, 60, 60])

        self.T['short'] = fuzz.trapmf(self.T.universe, [10, 10, 20, 25])
        self.T['medium'] = fuzz.trimf(self.T.universe, [20, 35, 50])
        self.T['long'] = fuzz.trapmf(self.T.universe, [40, 50, 60, 60])

    def rules(self):
        return [ctrl.Rule(self.V1['many'] & self.V2['few'], self.T['long']),
                ctrl.Rule(self.V1['few'] & self.V2['many'], self.T['short']),
                ctrl.Rule(self.V1['moderate'] & self.V2['moderate'], self.T['medium']),
                ctrl.Rule(self.V1['many'] & self.V2['many'], self.T['medium'])]

    def compute(self, v1_value, v2_value):
        self.simulator.input['V1'] = v1_value
        self.simulator.input['V2'] = v2_value
        try:
            self.simulator.compute()
            result = self.simulator.output['T']
            return result
        except KeyError as e:
            print(f"Error: {e}, possibly no rules fired for the given inputs.")
            return None

    def visualize(self, plots, nrows=1, ncols=1) -> None:
        num_plots = len(plots)
        fig, axs = plt.subplots(nrows, ncols, figsize=(8 * ncols, 4 * nrows))

        if nrows == 1 or ncols == 1:
            axs = np.array(axs).flatten()
        else:
            axs = axs.flatten()

        for ax, (plot_func, title) in zip(axs, plots):
            plot_func(ax)
            ax.set_title(title)
            ax.legend()

        for ax in axs[num_plots:]:
            fig.delaxes(ax)

        plt.tight_layout()
        plt.show()

    def plot_v1(self, ax:plt.Axes) -> None:
        ax.plot(self.V1.universe, self.V1['few'].mf, label='Few')
        ax.plot(self.V1.universe, self.V1['moderate'].mf, label='Moderate')
        ax.plot(self.V1.universe, self.V1['many'].mf, label='Many')

    def plot_v2(self, ax:plt.Axes) -> None:
        ax.plot(self.V2.universe, self.V2['few'].mf, label='Few')
        ax.plot(self.V2.universe, self.V2['moderate'].mf, label='Moderate')
        ax.plot(self.V2.universe, self.V2['many'].mf, label='Many')

    def plot_t(self, ax:plt.Axes) -> None:
        ax.plot(self.T.universe, self.T['short'].mf, label='Short')
        ax.plot(self.T.universe, self.T['medium'].mf, label='Medium')
        ax.plot(self.T.universe, self.T['long'].mf, label='Long')

if __name__ == "__main__":
    semaphore_system = SemaphoreSystem()

    result_a = semaphore_system.compute(35, 15)
    if result_a is not None:
        print(f"Green light time for 35 vehicles in Avenue 1 and 15 in Avenue 2: {result_a} seconds")

    result_b = semaphore_system.compute(20, 45)
    if result_b is not None:
        print(f"Green light time for 20 vehicles in Avenue 1 and 45 in Avenue 2: {result_b} seconds")

    plot_functions = [
        (semaphore_system.plot_v1, 'Membership Functions for V1 (Vehicles in Avenue 1)'),
        (semaphore_system.plot_v2, 'Membership Functions for V2 (Vehicles in Avenue 2)'),
        (semaphore_system.plot_t, 'Membership Functions for T (Green Light Time)')
    ]

    semaphore_system.visualize(plot_functions, nrows=2, ncols=2)