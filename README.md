conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt

mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt

streamlit run dashboard.py#   r e n t a l - b i k e - a n a l y s i s  
 