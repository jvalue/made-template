import abc


class Demographic(abc.ABC):
    def __init__(self):
        self._case_id = None
        self._age_at_index = None
        self._cause_of_death = None 
    
    @property
    def case_id(self):
        return self._case_id
    @case_id.setter
    def case_id(self, case_id):
        self._case_id = case_id
    
    @property
    def age_at_index(self):
        return self._age_at_index
    @age_at_index.setter
    def age_at_index(self, age_at_index):
        self._age_at_index = age_at_index
    
    @property
    def cause_of_death(self):
        return self._cause_of_death
    @cause_of_death.setter
    def cause_of_death(self, cause_of_death):
        self._cause_of_death = cause_of_death

    def as_dict(self):
        return {'case_id': self.case_id, 'age_at_index': self.age_at_index, 'cause_of_death': self.cause_of_death}
    
class Diagnosis(abc.ABC):
    def __init__(self):
        self._case_id = None
        self._ajcc_pathologic_t = None
        self._ajcc_pathologic_n = None
        self._ajcc_pathologic_m = None
    
    @property
    def case_id(self):
        return self._case_id
    @case_id.setter
    def case_id(self, case_id):
        self._case_id = case_id
    
    @property
    def ajcc_pathologic_t(self):
        return self._ajcc_pathologic_t
    @ajcc_pathologic_t.setter
    def ajcc_pathologic_t(self, ajcc_pathologic_t):
        self._ajcc_pathologic_t = ajcc_pathologic_t    

    @property
    def ajcc_pathologic_n(self):
        return self._ajcc_pathologic_n
    @ajcc_pathologic_n.setter
    def ajcc_pathologic_n(self, ajcc_pathologic_n):
        self._ajcc_pathologic_n = ajcc_pathologic_n

    @property
    def ajcc_pathologic_m(self):
        return self._ajcc_pathologic_m
    @ajcc_pathologic_m.setter
    def ajcc_pathologic_m(self, ajcc_pathologic_m):
        self._ajcc_pathologic_m = ajcc_pathologic_m

    def as_dict(self):
        return {'case_id': self.case_id, 'ajcc_pathologic_t': self.ajcc_pathologic_t, 'ajcc_pathologic_n': self.ajcc_pathologic_n, 'ajcc_pathologic_m': self.ajcc_pathologic_m}
