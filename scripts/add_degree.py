from applications.alumniprofile.models import Degree

degrees = ['Class 10th','Class 12th','Phd','M.Tech','B.Tech','M.Des','B.Des','MAcc', 'MAS', 'MEcon', 'MArch', 'MASc', 'MA', 'MAT', 'MA', 'MBus', 'MBA', 'MBI', 'MChem', 'MCom', 'MCA', 'MCJ', 'MDes', 'MDiv', 'MEcon', 'MEd', 'MEnt', 'MEng', 'MEM', 'LLM Eur', 'MFin', 'Master of Quantitative Finance', 'MFA', 'MHA', 'MHS', 'MH', 'MILR', 'MIS', 'MISM', 'MSIT', 'MJ', 'LLM', 'MSL', 'MArch', 'MLitt', 'MA', 'MLIS', 'MM', 'MM', 'OT', 'MPharm', 'MPhil', 'MPhys', 'MPS', 'MPA', 'MPAff', 'MPH', 'MPP', 'MRb', 'R', 'STM', 'MSM', 'MSc', 'MSE', 'MFin', 'HRD', 'MSMIS', 'MSIS', 'MSIT', 'MSN', 'MSPM', 'MSc', 'MSL', 'SCM', 'MST', 'MSW', 'MSSc', 'ChM', 'MSt', 'ThM', 'MTS', 'MVSC']

def add_degree() :
    print("Adding degree")
    try :
        degree_list = [Degree(degree = degree) for degree in degrees]
        Degree.objects.bulk_create(degree_list, ignore_conflicts=True)
        print("Degree added successfully")
    except Exception as e :
        print(f'An error occured: {e}')
        raise