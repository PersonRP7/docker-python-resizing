#Dockerized python resizing script.

##Usage:

1. Clone the project.

2. ```python
    docker-compose up -d
    ```

3. Place the images to be resized in the root of the cloned project.

4. Copy the image(s) into the container:

    4.a) For a single image:
            ```python
            python copy.py -d to -n image.jpg
            ```

     4.b) For multiple images:
            ```python
            python copy_all.py -d to
            ```

5. Enter the docker container using:
        ```python
        docker exec -it thumbnail sh
        ```

6. Engage the interactive resizing script using:
        ```python
        python thumbnail.py
        ```

The script requires three values:

    1. Quality
    2. Height
    3. Width

Press enter to input default values:
    1. 100
    2. 100
    3. 100

7. Exit the docker container (Ctrl + D).

8. Copy the image(s) from the container into the root project directory:

8.a) For a single image:

    ```python
        python copy.py -d from -n image_resized.jpeg
    ```

    8.b) For multiple images:

    ```python
        python copy_all.py -d from
    ```

        


    

    

