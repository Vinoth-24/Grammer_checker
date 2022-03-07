# Grammer_checker
This app is designed to check the grammatical accuracy of the sentence as well as to correct the wrong grammar in sentences.<br>
The app uses a Pre-trained model to find typographical and grammatical error in a sentence.<br>
Pretrained model used - https://github.com/PrithivirajDamodaran/Gramformer#correcter-with-qe-estimator---available-now <br
Accuracy technique : Length of a sentence vs No. of grammatical errors found in that sentence. ((len(x["text"]) - len(x["edit_col"]))/len(x["text"]))*100 <br>
Output : In the form of Dataframe with resultant text in "corrected_text" and accuracy in "accuracy %" <br>
Deployed using Streamlit library<br>
