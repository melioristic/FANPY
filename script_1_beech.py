from fanpy import Formind

model_path = '/data/compoundx/FORMIND/linux_models/'	
par_file_name='beech'
project_path='/data/compoundx/FORMIND/Project_Beech/'


num_sim = 1
model = Formind(model_path, project_path, par_file_name)
sim_id = 'general'
model.run(sim_id=sim_id, num_sim=num_sim)