#! /bin/bash

docker run --gpus all -it --rm --net=host -v $(pwd):/home -w /home --name terrain_flow_running terrain-flow jupyter notebook --allow-root
