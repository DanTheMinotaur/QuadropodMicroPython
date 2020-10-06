
### Setup

Make port writable 

```bash
sudo chmod 777 /dev/ttyUSB0
```

### Test Functions

#### Test single motor using degrees

```python

from app import utils

u = utils.Utils()

motor_index = 0
degrees = 90
u.test_servo_motor(motor_index, degrees)
```
