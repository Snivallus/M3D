from .dataset_info import dataset_info
from .multi_dataset import ITRDataset
from .prompt_templates import Caption_templates, PosREC_templates, PosREG_templates
from .term_dictionary import term_dict 

__all__ = ["dataset_info", 
           "ITRDataset", 
           "Caption_templates", "PosREC_templates", "PosREG_templates" , 
           "term_dict"]