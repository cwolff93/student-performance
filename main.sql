-- Get the average exam score filtering by students who have extracurricular activies and hours studied above 10

SELECT hours_studied, 
	AVG(exam_score) AS avg_exam_score
FROM student_performance
WHERE extracurricular_activities = 'Yes' AND hours_studied > 10
GROUP BY hours_studied
ORDER BY hours_studied DESC

-- Create a new column with ranges of studied hours and show average exam score according to these ranges
  
SELECT 
	CASE
		WHEN hours_studied BETWEEN 1 AND 5 THEN '1-5 hours'
		WHEN hours_studied BETWEEN 6 and 10 THEN '6-10 hours'
		WHEN hours_studied BETWEEN 11 and 15 THEN '11-15 hours'
		ELSE '16+ hours' 
	END AS hours_studied_range,
	AVG(exam_score) AS avg_exam_score
FROM student_performance
GROUP BY hours_studied_range
ORDER BY AVG(exam_score) DESC

-- Display the 30 first lines of the requested columns sorted by exam dense rank over exam scores
  
SELECT 
	attendance, 
	hours_studied, 
	sleep_hours, 
	tutoring_sessions, 
	DENSE_RANK () OVER(ORDER BY exam_score DESC) AS exam_rank -- DENSE_RANK() doesn't skip rank numbers like RANK()
FROM student_performance
LIMIT 30
