# Data Science Methodologies: Making Business Sense

This is the repository for the LinkedIn Learning course Data Science Methodologies: Making Business Sense. The full course is available from [LinkedIn Learning][lil-course-url].

![Data Science Methodologies: Making Business Sense][lil-thumbnail-url] 
There is an increasing recognition that data science needs to go beyond small-scale experimentation to a large-scale implementation. In this course, Neelam Dwivedi brings software engineering and data mining methodologies to data scientists, then applies these ideas by taking a simple business need through an entire life cycle—hosting a model, consuming it in a web application, and setting up its CI/CD pipeline. Neelam begins by explaining the methodologies used in the course and how they are combined. She shows you where to begin in developing architecture and deploying a model, then explains how larger web applications may consume the model as a service. Neelam covers how to stage your model and the app, as well as how to plan ahead with an overall roadmap. She concludes with thoughts on how to further applications of data science methodologies.

## Instructions
This repository has branches for each of the videos in the course. You can use the branch pop up menu in github to switch to a specific branch and take a look at the course at that stage, or you can add `/tree/BRANCH_NAME` to the URL to go to the branch you want to access.

There are four GitHub repositories for this course:

- https://github.com/LinkedInLearning/dsm-bank-model-2870047
- https://github.com/LinkedInLearning/dsm-bank-app-2870047
- https://github.com/LinkedInLearning/dsm-car-model-2870047
- https://github.com/LinkedInLearning/dsm-car-app-2870047

## Branches
The branches are structured to correspond to the videos in the course. The naming convention is `CHAPTER#_MOVIE#`. As an example, the branch named `02_03` corresponds to the second chapter and the third video in that chapter. 
Some branches will have a beginning and an end state. These are marked with the letters `b` for "beginning" and `e` for "end". The `b` branch contains the code as it is at the beginning of the movie. The `e` branch contains the code as it is at the end of the movie. The `main` branch holds the final state of the code when in the course.

When switching from one exercise files branch to the next after making changes to the files, you may get a message like this:

    error: Your local changes to the following files would be overwritten by checkout:        [files]
    Please commit your changes or stash them before you switch branches.
    Aborting

To resolve this issue:
	
    Add changes to git using this command: git add .
	Commit changes using this command: git commit -m "some message"


### Instructor

**Neelam Dwivedi**

_Assistant Teaching Professor at Heinz College_

Check out my other courses on [LinkedIn Learning](https://www.linkedin.com/learning/instructors/neelam-dwivedi?u=104).

[lil-course-url]: https://www.linkedin.com/learning/data-science-methodologies-making-business-sense
[lil-thumbnail-url]: https://cdn.lynda.com/course/2870047/2870047-1617217319959-16x9.jpg
