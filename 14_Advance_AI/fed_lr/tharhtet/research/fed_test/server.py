"""tharhtet: A Flower / TensorFlow app."""
import flwr as fl
from flwr.common import Context, ndarrays_to_parameters
from flwr.server import ServerApp, ServerAppComponents, ServerConfig
from flwr.server.strategy import FedAvg
import tf_data_and_model



def server_fn(context: Context):
    # Read from config
    num_rounds = context.run_config["num-server-rounds"]

    # Get parameters to initialize global model
    parameters = ndarrays_to_parameters(tf_data_and_model.load_model().get_weights())

    # Define strategy
    strategy = strategy = FedAvg(
        fraction_fit=1.0,
        fraction_evaluate=1.0,
        min_available_clients=2,
        initial_parameters=parameters,
    )
    config = ServerConfig(num_rounds=num_rounds)

    return ServerAppComponents(strategy=strategy, config=config)

# Create ServerApp
app = ServerApp(server_fn=server_fn)
fl.server.start_server(server_address = "0.0.0.0:8080",)