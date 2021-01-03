## Chapter-19
### Practice questions
1. What is an RGBA value?\
**Answer:**\
It is a tuple of four integers from 0 to 255.These four integers corresponds to the amount of red,green,blue.

2. How can you get the RGBA value of 'CornflowerBlue' from the Pillow module?\
**Answer:**\
ImageColor.getcolor('CornflowerBlue', 'RGBA')

3. What is a box tuple?\
**Answer:**\
It is a tuple of four integers the left-edge x-coordinate, the top-edge y-coordinate, the width, and the height.

4. What function returns an Image object for, say, an image file named zophie.png?\
**Answer:**\
Image.open('zophie.png')

5. How can you find out the width and height of an Image object’s image?\
**Answer:**\
 imageObj.size
 
6. What method would you call to get Image object for a 100×100 image, excluding the lower-left quarter of it?\
**Answer:**\
imageObj.crop((0, 50, 50, 50)) 

7. After making changes to an Image object, how could you save it as an image file?\
**Answer:**\
imageObj.save()

8. What module contains Pillow’s shape-drawing code?\
**Answer:**\
ImageDraw

9. Image objects do not have drawing methods. What kind of object does? How do you get this kind of object?\
**Answer:**\
ImageDraw objects have shape-drawing methods such as point(), line(), or rectangle(). They are returned by passing the Image object to the ImageDraw.Draw() function.
