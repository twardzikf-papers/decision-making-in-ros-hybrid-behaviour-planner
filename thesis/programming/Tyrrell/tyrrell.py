class TyrrellActivationAlgorithmDivided(UniformActivationAlgorithm):
    def _total_activation_divided_by_number_of_inputs(self, total_activation, amount_inputs):
        return total_activation / amount_inputs
    
class TyrrellActivationAlgorithmNotDivided(TyrrellActivationAlgorithmDivided):
    def _total_activation_divided_by_number_of_inputs(self, total_activation, amount_inputs):
        return total_activation

class TyrrellActivationAlgorithmAveraged(TyrrellActivationAlgorithmDivided):
    def _total_activation_divided_by_number_of_inputs(self, total_activation, amount_inputs):
        return (total_activation / 2 * amount_inputs) + (total_activation / 2)