# PNG image generator. 

Generates images combining other png files. 

To run yu need to create the folder `img` and inside that directory place  `background`, `extra` and `main`. The last 3 directories must contain the images to merge. Run the function `genera_imagenes()` to generate 10 images. Runs are deterministic because we set the seed of the rng. Output will create 2 folders, one containing the images and the second containing the metadata of each image. 

## genera_imagenes(num = 10, rng_seed = 1)

Generates `num` images using seed `rng_seed`. 


## probas_por_objeto()

After generating the images you can check how many got each attribute by running this function. 3 graphs will be desplayed. 

## histograma_rng(num=100,rng_seed=1,cant=8)

Displays a histogram of all the number frecuencies (from 0 to cant-1) that the rng with the given seed generates on an iteration of `num` random numbers. 