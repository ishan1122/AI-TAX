from qiskit import Aer
from qiskit.utils import QuantumInstance
from qiskit.ml.algorithms import QSVM
from qiskit.ml.datasets import ad_hoc_data

# Load dataset
feature_dim = 2  
train_data, train_labels, test_data, test_labels = ad_hoc_data(training_size=20, test_size=10, n=feature_dim)

# Quantum simulator
quantum_instance = QuantumInstance(Aer.get_backend('qasm_simulator'))

# Train Quantum Support Vector Machine (QSVM)
qsvm = QSVM(quantum_instance=quantum_instance)
qsvm.fit(train_data, train_labels)

# Make predictions
predictions = qsvm.predict(test_data)
print("✅ Quantum AI Fraud Predictions:", predictions)
