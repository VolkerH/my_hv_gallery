# About this folder

The files in this folder are to experiment with running a web server that dynamically generates "thumbnail" images and serves them to a browser. 

# Background

Many of the interactive examples in this repository rely on embedding images for hovertools or galleries to be rendered as HTML. Therefore they need to be embedded with an `<img src=....>` tag and have a URL to the image. So far I had precomputed images, which may use a lot of space. Also the file formats supported by HTML rendering engines are typically 8-bit gif, png, jpg. Browsers typically can't render 12bpp or 16bpp data that we get from some microscopes.

Therefore it would be nice to generate preview images for the browser on the fly. In the http request one would pass the ID of the source image, which could be 16bit tiff or anything supported by Bioformats, the bounding box crop and potentially and overlay (segmentation mask). The web server than would read the source image and pass back the rendered jpg (or png). 

One could also specify a target intensity range in the URL.



volker hilsenstein @ embl de 
