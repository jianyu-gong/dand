# Data Visualization Project - Flight Delay(2008)

## Summary
A data set which contains information on United flight delays and performance from RITA in 2008 is studied. The variables - carrier name, arrival delay, departure delay and the day of week are examed. The data set is summarized and transformed by Pandas in Jupyter Notebook. Based on the visualization, it can be clearly found which carrier has the best performance and which day of week is the least likely to be delayed. 

## Design
As three variables - arrival delay in minutes, the percent of delayed flight and carrier name are required to find the best performance company, bubble chart is suitable to present the story. X-axis is used to show the average delay time in minutes and y-axis is used to show the percentage of delayed flight. Thus, the best performance carrier should appear at the bottom-left corner of the chart. 

In addition, the distribution of percent of delayed flight among the day of week is also studied. The barplot is selected. X-axis is used to present the day of week and the y-axis is used to present the percentage of delayed flight. The day of week having the smallest percentage of delayed flight should be the lowest bar.

The bubble chart and bar plot are modified based on feedbacks as showning below:
* Remove the grids in bubble chart;
* Add a legend to bubble chart;
* Use departure delay time to repsent the size of the bubble;
* Tried to change the bar color to light blue but the color of dash line is changed as well;
* Add a tittle to each plot;

## Feedback
I sent my plots to three friends and asked for some feedbacks. The feedbacks are summarized as below:
* Feedback 1
> It is clear to see the bubble distribution however the grid in the bubble chart make the chart a little messy. As the animation already shows the dash lines towards two axis, the grid may be not necessary. Also, it is good to have a legend in bubble chart becasue the readers may not understand what does the color stand for. The bar plot seems good to me.

* Feedback 2
> I would recommend you add a legend in bubble chart. In that case, I can have a overall idea about all the carrier without putting my mouse on every circle. Also, you did not use the area of circle to show any information. Maybe use the size of the bubble to give readers more information. Adding tittles maybe good also?

* Feedback 3
> I noticed that the color of the bar plot is a little tricky. The colors of the bar and animation dash line are almost same. Therefore, when I put my mouse on Saturday bar or Wednesday bar, I cannot see the dash line clearly. Can you change the color to make the dash line more obvious. 
