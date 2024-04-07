Here is an example of a project for Dr. Sarah Westcott UCSF. This is an initial discussion to see if Race has an effect on a range different medical outcomes. 
The scope of this data and the lack of power in the study leads to a significant risk of overfitting, and discovering a significant result to to the number of statistical tests performed. For the categorical variables a chi squared test was used. For the numberic variables a t test was used.

Both of the test's are 2 sided to determine if there is any expected difference in the outcome.

The different files in this repository are the following. 


-"prelim tables takotsubo april_19_23.docx" This is the scope of the variables that will be included in the final analysis and also displays the format the result should be presented in. 

-"data_2.csv" the data collected during the scientific study. 75 Particitpants with 260 data points per participent.

-"test_mapping.xlsx" The mapping from the outcome's medical name and its corresponding column  in the data set. This is a mapping for the 47 medical outcomes the analysis focused on. 

-"Codebook_Takotsubo Data Form _ REDCap.pdf" contains a discription the data collected in the study for each column included in the data. 

-"P_value_calc.py" the python script filtering the required data through the provided mapping. This script applies the required summary, t-test, or chi squared test to the variables depending on the variables circustances. 

