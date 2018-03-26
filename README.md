# Production Machine Learning

## Test-Driven Development
Pytest for Unit Tests and TravisCI for Continuous Integration

Run tests with cmd: pytest in terminal from production-ml folder.

## About
I used Python and pytest to build a Production Machine Learning App that loads data, preprocesses it, and provides preliminary EDA (Exploratory Data Analysis).

## Learnings
- Used Pytest to test Matplotlib's plotting, had to override object's equal function and configure Travis's VM to make this successful
- Made EDA object Immutable: analytic functions return new EDA objects on the fly with different configurations
- Extensibility: Currently the project supports Structured Data, but the app architecture is extendable to Unstructured Data as well. In particular, text and images will also have their own preprocess and EDA objects.
- Made use of delegation: The Dataset object delegates to Preprocess, which delegates to EDA
- StructuredDataApp has Dataset, Features, Model, Train, and Eval functions
