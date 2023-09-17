# Brand_Logo_Detection_VISIOPE
Our project consists in  the implementation of an open set logo detector and retrieval.

We have chosen this task because it has many applications in real world problems. 
In fact automated search for logos is a desirable task in visual image analysis. In particular in tv broadcasting or events to understand the effectiveness measurement of advertisements.
This task can be very useful for companies, because being able to find all logos in images that match a logo of a specific company, allows to assess the visual frequency and prominence of logos in TV broadcasts and evaluate sponsorship convenience for a company.
From the point of view of computer vision this is a quite challenging problem too, because we want to detect very small objects in images, with different perspectives, brightness and distortions. The images we are working with are low quality real world images, so detecting small objects is even more difficult.

The project was divided in two main stages: the detection stage, where we developed a model capable of detecting logos in input images, and then the retrieval stage, where, given a query sample in the shape of a reference logo image, the task was to find further occurrences of this logo in a certain image.

The dataset that we used for developing this task is Logos in the Wild Dataset. Since it is very large, and we wanted flexibility from our model we focused on open set logo retrieval.
[immagine]
We used Faster R-CNN and YOLOv4 and YOLOv7 as detector obtaning this results:
[immagine]

For the retrival we encoded the detected logos and the reference one with ResNet-18, then we used cosine similarity to obtain similarity scores:
[image]

References:
[Open Set Logo Detection and Retrival](https://arxiv.org/pdf/1710.10891.pdf)https://arxiv.org/pdf/1710.10891.pdf),

[Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks](https://arxiv.org/abs/1506.01497),

[You Only Look Once: Unified, Real-Time Object Detection](https://arxiv.org/abs/1506.02640)
 
