<!DOCTYPE html>
<html>
<title>Matting and cutting</title>

<head>
<!--<meta charset="UTF-8">-->
<meta name="keywords" content="frame,mat,print,Lightroom,GIMP">
<meta name="author" content="Serge Yuschenko">
</head>

<body>

<h1>Matting and cutting</h1>

<p>There are two ways of matting a picture. The first one when you have a picture and cut a mat to exactly fit the picture. The second one, when you already have a pre-cut mat or a frame, and want to fit a picture into it. In the second case the mat may not have the exactly the same size or aspect ratio as the picture. So you will have to crop it. The question is how much of your precious image you are willing to sacrifice? For instance, if your mat cut off area is 10 ?”x15 ?” it is perfect for 11”x16” prints with a ?” border. If nobody prints 11”x16” in your neighborhood the only choice is s 12”x18” with a massive cropping in both directions.</p>

<left>
<img style="margin-left: 100px;" width="700" src="https://drive.google.com/uc?id=0B2HqsMfLrhkgQV9xVURxVzZBZW8" />
</left>

<p>Obviously the cropping may be minimized by adding a border around the image.</p>

<left>
<img style="margin-left: 100px;" width="700" src="https://drive.google.com/uc?id=0B2HqsMfLrhkgZlI2MU1HSUh5R3c" />
</left>

<p>It is an easy math to figure out the border width in inches (or millimeters), but the border must be added in a software. Thus you must convert inches to pixels depending on the picture dimensions. This is not a rocket science as well, but takes slightly longer. If you are preparing a number of pictures of different size, the repeating calculations may become annoying. I automated the calculation with <a href="https://drive.google.com/uc?id=0B2HqsMfLrhkgdGtiMTJpMTUtelk" target="_blank">an Excel spreadsheet</a>. The cells in the sheet are self-explanatory, but perhaps it is too much information there. I put there everything in case if I need to do some troubleshooting. You may disregard most of that data. All you need is column B.</p>

<left>
<img style="margin-left: 100px;" width="200" src="https://drive.google.com/uc?id=0B2HqsMfLrhkgVXo1RnZqOEVnUlk" />
</left>

<p>The workflow is:</p>
1.	Enter the print dimensions to B1 and B2<br>
2.	Enter the cut out (window) dimensions to B3 and B4<br>
3.	Enter your image dimensions to B5 and B6<br>
4.	From B8 take the number of pixels to add on left and right<br>
5.	From B9 take the number of pixels to add on top and bottom<br>

<p>What you are going to do with these numbers depends on the software you use. There are a number of framing plugins for LightRoom (I use L/R Mogrify 2).</p>

<left>
<img style="margin-left: 100px;" width="400" src="https://drive.google.com/uc?id=0B2HqsMfLrhkgZGNPVHQzWV9PZzQ" />
</left>

<p>I also wrote <a href="https://drive.google.com/uc?id=0B2HqsMfLrhkgbXU0VW5yUkctOWs" target="_blank">a simple plugin for GIMP</a> that can be accessed via Image->Add Print Borders.</p>

<left>
<img style="margin-left: 100px;" width="400" src="https://drive.google.com/uc?id=0B2HqsMfLrhkgM1J0X3F6aE4xV1U" />
</left>

<body/>
