#hunger-project
docker build -t baseline-sampling .  # run this only once <br>
docker run --rm -v "$(pwd):/app" baseline-sampling python sampling.py # Run this everytime to run the code