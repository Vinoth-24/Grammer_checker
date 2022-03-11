# Grammer_checker
- This app is designed to check the grammatical accuracy of the sentence as well as to correct the wrong grammar in sentences.<br>
- The app uses a Pre-trained model to find typographical and grammatical error in a sentence.<br>
- Pretrained model used - https://github.com/PrithivirajDamodaran/Gramformer#correcter-with-qe-estimator---available-now <br
- Accuracy technique : Length of a sentence vs No. of grammatical errors found in that sentence. ((len(x["text"]) - len(x["edit_col"]))/len(x["text"]))*100 <br>
- Output : In the form of Dataframe with resultant text in "corrected_text" and accuracy in "accuracy %" <br>
- Deployed using Streamlit library<br>
- You can download once the correction has been made for the dataset.
- This is only made for local deployment. You can ofcourse try reproducing it with the requirements file and the code that I have addded.
- I have added the final csv file after checking grammer with acc in this repo. I have used 1/3 of the total dataset as the process was taking too much time and my laptop is not a high end one. Hope you can understand!
### Have a good day!
