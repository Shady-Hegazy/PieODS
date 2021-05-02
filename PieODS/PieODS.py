# import .Adapter
# import .Pipeline
# import .Notification
# import .Storage
from . import Adapter
from . import Pipeline
from . import Notification
from . import Storage

ad = Adapter.AdapterAPI()
ds = Adapter.DatasourceAPI()
pl = Pipeline.PipelineAPI()
nt = Notification.NotificationAPI()
st = Storage.StorageAPI()

class DataSource():
    pass