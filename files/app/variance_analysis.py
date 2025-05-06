class VarianceAnalysis:
    def __init__(self, actual, forecasted):
        self.actual = actual
        self.forecasted = forecasted

    def calculate_variance(self):
        return self.actual - self.forecasted

    def explain_variance(self, threshold=0.05):
        variance = self.calculate_variance()
        explanation = {}
        for index, value in enumerate(variance):
            if abs(value) > threshold:
                explanation[index] = f"Significant variance detected: {value}"
        return explanation