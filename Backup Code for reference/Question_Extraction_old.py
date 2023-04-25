## Approach 1 Updated code (for single file) : Testing
import pandas as pd
from docx import Document
import re
import os
import tqdm
import nltk
from nltk.tokenize import word_tokenize
nltk.download('averaged_perceptron_tagger')

class Extraction:
    def word_to_pdf(self, file_name, name):
        """ 
        This code defines a function word_to_pdf that takes a word doc / docx file as input and returns a pdf file.
            """
        new_name = file_name.replace("."+name, r".pdf")
        in_file = os.path.abspath(file_name)
        pdf_filename = os.path.abspath(new_name)
        word = client.DispatchEx("Word.Application")
        doc = word.Documents.Open(in_file)
        doc.SaveAs(pdf_filename, FileFormat = 17)
        doc.Close()
        word.Quit()
        return pdf_filename

    def input_file(self, file_name):
        """ 
        This code defines a function input_file that takes a file as input and will send it to another function (i.e.word_to_pdf) 
        to convert into pdf if it is in .doc/.docx format and returns the pdf file name. 
            """
        try:
            match=0
            if file_name.endswith(".doc"):
                name,match= "doc",1
                return word_to_pdf(file_name,name)
            elif file_name.endswith(".docx"):
                name,match= "docx",1
                return word_to_pdf(file_name,name)
            elif file_name.endswith(".pdf"):
                pdf_filename=os.path.abspath(file_name)
                return pdf_filename
            elif not file_name.endswith(".doc") or not file_name.endswith(".docx") or not file_name.endswith(".pdf"):
                print("Unsupported file format. Please provide the file which is in either in doc or docx or pdf format")
                sys.exit()

        except Exception:
            print("An error occured during in the file conversion function")


    def detect_question_or_request(self, sentence):
        """ 
        This code defines a function detect_question_or_request that takes a sentence as input and returns a string indicationg whether
        the sentence is a question, request, or statement.

            Ex: Input 1: What is the annual revenue of your company ?
            Output: Question
            Input 2: Brief history of your company.
            Output: Request 
            """
        # Tokenize the sentence
        question_words=['what', 'when', 'where', 'who', 'whom', 'which', 'whose', 'why', 'how','how long','how many','how much','how far','how often','have','has','do','did','does']
        verbs_and_modal_verbs=["can", "could", "will", "would", "may", "might", "shall", "should", "must",'please','define','describe','outline','provide','brief','summarise','explain','submit','propose','write','detail','discuss']
        tokens = [token.lower() for token in word_tokenize(sentence)]         

        # Check if sentence ends with a question mark or sentence contains any question words
        if sentence.strip().endswith("?") or any(sentence.lower().startswith(word) for word in question_words):
            return "Question"
        # Check if sentence starts with a verb or modal verb
        elif tokens[0].lower() in verbs_and_modal_verbs:
            return "Request"
        else:
            return "Statement"


    def question_search(self, file):
        """ 
        This code defines a function question_search that takes a file as input and returns two outputs. One is a dataframe indicationg whether
        the sentence is a question, request, or statement and other one is list which is having all the questions and request sentences

            Ex: Input 1: file which is docx format
            Output 1: dataframe consists of two columns (Sentence, Sentence Type)
            Output 2: List consists of questions and request sentences 
            """

        questions = []
        results={}
        unwanted_questions=["please also refer to appendix","please see appendix","Appendix"]
        text = ""
        doc = fitz.open(file)
        for page in doc:
            text += page.get_text()
        new_text=re.sub(r"\n([a-z])",r"\g<1>",text)
        paragraphs=new_text.split('\n')
        paragraphs = [para.strip() for para in paragraphs] # To remove white space
        paragraphs = [para for para in paragraphs if len(para)>8] # To remove if sentence having only symbols/numbers/lessthan 8 characters

        for paragraph in paragraphs:
            if re.search('[a-zA-Z]+',paragraph) !=None: # To filter paragraphs which doesn't have any letters
                paragraph=paragraph[re.search(r"[a-zA-Z]",paragraph).start():] # To remove numbers or symbols at start of paragraph
                # Looping through each paragraph to find whether it is a question or request or statement
                if detect_question_or_request(paragraph)== "Question" or detect_question_or_request(paragraph)== "Request":
                    results[paragraph]=detect_question_or_request(paragraph)
                else:
                    results[paragraph]="Statement"
                    questions.append(paragraph)

        # To see the result dataframe of all the sentences (question or request or statement) 
        df_results=pd.DataFrame(list(results.items()),columns=['Sentence','Sentence_type']) 

        # To see the questions and requets in the form of list of sentences
        questions_list = df_results.loc[(df_results['Sentence_type']=='Question') | (df_results['Sentence_type']=='Request')]['Sentence'].values.tolist()
        questions_list_filtered=[ques for ques in questions_list if not any(re.search(un_ques, ques, re.IGNORECASE) for un_ques in unwanted_questions)] # To remove unwanted sentences
        questions_list_filtered=[ques_1 for ques_1 in questions_list_filtered if len(ques_1.split())>2] # To remove short questions (i.e. lessthan two words)
        return df_results, questions_list_filtered  
