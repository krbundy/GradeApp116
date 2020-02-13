# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 12:17:13 2020

@author: kenne
"""

from wtforms import (Form, validators,SubmitField,DecimalField)

import numpy as np

from flask import Flask
from flask import request
from flask import render_template


class ReusableForm(Form):
    
    
    #Grade entries
    
    test_one_score = DecimalField("Enter First Exam Percentage", 
                                  validators=[validators.InputRequired(),
                                              validators.NumberRange(min=0.0, 
                                                                     max=120.0, 
                                                                     message = 'Score must be betwoeen 0 and 120')])
    
    test_two_score = DecimalField("Enter Second Exam Percentage", 
                                  validators=[validators.InputRequired(),
                                              validators.NumberRange(min=0.0, 
                                                                     max=120.0, 
                                                                     message = 'Score must be betwoeen 0 and 120')])
    
    test_three_score = DecimalField("Enter Third Exam Percentage", 
                                  validators=[validators.InputRequired(),
                                              validators.NumberRange(min=0.0, 
                                                                     max=120.0, 
                                                                     message = 'Score must be betwoeen 0 and 120')])
    
    
    test_four_score = DecimalField("Enter Fourth Exam Percentage", 
                                  validators=[validators.InputRequired(),
                                              validators.NumberRange(min=0.0, 
                                                                     max=120.0, 
                                                                     message = 'Score must be betwoeen 0 and 120')])
    
    final_exam_score = DecimalField("Enter Final Exam Percentage", 
                                  validators=[validators.InputRequired(),
                                              validators.NumberRange(min=0.0, 
                                                                     max=120.0, 
                                                                     message = 'Score must be betwoeen 0 and 120')])
    
    
    quiz_average = DecimalField("Enter Average Quiz Grade", 
                                  validators=[validators.InputRequired(),
                                              validators.NumberRange(min=0.0, 
                                                                     max=120.0, 
                                                                     message = 'Score must be betwoeen 0 and 120')])
    
    homework_average = DecimalField("Enter Average Homework Grade", 
                                  validators=[validators.InputRequired(),
                                              validators.NumberRange(min=0.0, 
                                                                     max=120.0, 
                                                                     message = 'Score must be betwoeen 0 and 120')])
    
    attendance_score = DecimalField("Enter Attendance Grade", 
                                  validators=[validators.InputRequired(),
                                              validators.NumberRange(min=0.0, 
                                                                     max=120.0, 
                                                                     message = 'Score must be betwoeen 0 and 120')])
    
    video_quiz_average = DecimalField("Enter Video Quiz Average", 
                                  validators=[validators.InputRequired(),
                                              validators.NumberRange(min=0.0, 
                                                                     max=120.0, 
                                                                     message = 'Score must be betwoeen 0 and 120')])
    project_score = DecimalField("Enter Project Average", 
                                  validators=[validators.InputRequired(),
                                              validators.NumberRange(min=0.0, 
                                                                     max=120.0, 
                                                                     message = 'Score must be betwoeen 0 and 120')])
    
    
    #Submit button
    submit = SubmitField("Calculate")
    
    



app=Flask(__name__)

#Homepage for the app
@app.route("/",methods=['GET','POST'])
def home():
    form=ReusableForm(request.form)
    
    if request.method=='POST' and form.validate():
        
        #Extract all of the data fields from the webform
        exam_one_score = request.form['test_one_score']
        exam_two_score = request.form['test_two_score']
        exam_three_score = request.form['test_three_score']
        exam_four_score = request.form['test_four_score']
        final_exam_score = request.form['final_exam_score']
        attendance_score = request.form['attendance_score']
        homework_average = request.form['homework_average']
        quiz_average = request.form['quiz_average']
        video_quiz_average = request.form['video_quiz_average']
        project_score = request.form['project_score']
        
        #grades = np.array((exam_one_score,exam_two_score,exam_three_score,exam_four_score,final_exam_score,
        #                   homework_average,quiz_average,attendance_score),dtype=np.float32)
        #
        #weights = np.array((0.1,0.1,0.1,0.1,0.2,0.1,0.1,0.1),dtype=np.float32)
        
        course_grade = float(np.dot(np.array((exam_one_score,exam_two_score,exam_three_score,exam_four_score,final_exam_score,
                           homework_average,quiz_average,attendance_score,video_quiz_average,project_score),dtype=np.float32).reshape((1,10)), 
                                    np.array((0.1,0.1,0.1,0.1,0.2,0.1,0.1,0.05,0.05,0.1),dtype=np.float32).reshape((10,1))))
        
        return render_template('filled.html', input=str(course_grade))
    
    
    
    return render_template('index.html',form=form)
    

app.run(host='0.0.0.0',port=5000)
