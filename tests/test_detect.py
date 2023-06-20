import pytest
from almavik.src.detectorDrop import detectorDrop
import numpy as np

def calculate_mse(expected, actual):
    expected = np.array(expected)
    actual = np.array(actual)
    mse = np.mean((expected - actual) ** 2)
    return mse

def test_detectorDrop_lists_length():
    images_folder = "./exp1"

    detector = detectorDrop(images_folder)

    assert len(detector.center_mass) == len(detector.img) == len(detector.img_contour) == 401
    ideal = [(546, 289), (546, 291), (546, 293), (546, 295), (546, 297), (547, 299), (550, 307), (550, 309), (550, 311), (550, 313), (546, 308), (548, 311), (546, 311), (547, 313), (546, 314), (546, 315), (546, 316), (547, 317), (548, 319), (548, 320), (548, 321), (546, 321), (546, 321), (546, 322), (546, 323), (546, 324), (546, 324), (546, 325), (546, 325), (546, 326), (546, 327), (549, 328), (548, 328), (550, 328), (550, 329), (549, 329), (550, 329), (549, 329), (550, 330), (549, 328), (549, 328), (548, 329), (548, 328), (549, 329), (550, 329), (550, 329), (549, 329), (549, 329), (549, 328), (550, 329), (549, 328), (549, 328), (548, 328), (550, 328), (549, 327), (553, 331), (553, 331), (545, 331), (545, 331), (550, 326), (549, 326), (552, 327), (545, 332), (546, 332), (552, 327), (552, 326), (550, 325), (551, 326), (550, 325), (550, 324), (551, 324), (550, 324), (550, 323), (552, 322), (552, 321), (551, 319), (552, 318), (551, 316), (551, 315), (551, 314), (551, 313), (552, 312), (551, 310), (551, 309), (552, 307), (550, 304), (550, 303), (550, 303), (550, 302), (551, 298), (551, 298), (551, 297), (552, 295), (552, 294), (552, 294), (552, 295), (552, 294), (553, 291), (553, 291), (554, 289), (553, 289), (552, 288), (554, 287), (553, 287), (553, 287), (554, 286), (553, 286), (553, 286), (554, 284), (553, 285), (553, 284), (553, 284), (554, 283), (554, 283), (554, 284), (554, 284), (555, 282), (554, 283), (554, 284), (554, 283), (554, 282), (554, 282), (554, 281), (554, 281), (554, 281), (555, 281), (555, 282), (555, 281), (555, 281), (555, 282), (555, 282), (555, 282), (555, 282), (555, 283), (555, 283), (555, 283), (555, 283), (555, 284), (555, 284), (555, 284), (555, 285), (555, 285), (555, 285), (555, 287), (555, 287), (556, 287), (555, 288), (555, 288), (554, 289), (555, 289), (554, 290), (556, 289), (556, 290), (556, 290), (555, 291), (555, 291), (556, 291), (555, 293), (555, 293), (557, 296), (557, 297), (557, 298), (556, 300), (556, 301), (555, 302), (555, 303), (555, 304), (555, 305), (555, 305), (556, 307), (557, 308), (556, 307), (555, 308), (555, 309), (556, 309), (556, 310), (557, 312), (557, 313), (557, 314), (555, 308), (556, 309), (555, 310), (555, 311), (555, 313), (555, 313), (555, 315), (555, 317), (555, 319), (555, 318), (556, 319), (555, 321), (555, 322), (560, 326), (560, 327), (560, 329), (560, 331), (555, 327), (555, 327), (555, 328), (556, 328), (555, 328), (556, 328), (555, 329), (555, 328), (555, 328), (556, 327), (555, 327), (556, 328), (555, 328), (556, 328), (556, 329), (554, 328), (555, 329), (555, 329), (554, 329), (555, 330), (554, 330), (554, 330), (554, 330), (553, 330), (553, 330), (553, 330), (554, 330), (552, 330), (552, 330), (553, 330), (553, 330), (553, 330), (554, 330), (555, 331), (561, 335), (556, 331), (561, 334), (560, 333), (559, 332), (559, 332), (554, 327), (560, 331), (559, 330), (559, 330), (560, 330), (559, 330), (559, 330), (555, 326), (555, 326), (554, 325), (554, 324), (552, 322), (553, 322), (553, 321), (551, 320), (551, 319), (551, 318), (551, 316), (551, 315), (552, 314), (549, 312), (550, 310), (549, 310), (550, 310), (550, 307), (551, 306), (552, 306), (552, 306), (551, 306), (551, 305), (551, 305), (552, 303), (550, 305), (550, 306), (550, 303), (549, 303), (548, 303), (549, 302), (548, 302), (547, 301), (547, 301), (547, 301), (548, 299), (547, 299), (547, 298), (547, 298), (547, 298), (549, 301), (547, 299), (548, 301), (549, 300), (546, 298), (547, 298), (548, 299), (549, 301), (549, 302), (549, 302), (549, 302), (547, 301), (547, 301), (547, 301), (548, 301), (547, 302), (547, 302), (546, 303), (547, 303), (547, 303), (547, 303), (547, 303), (546, 304), (547, 304), (547, 305), (547, 305), (548, 306), (548, 307), (547, 307), (548, 309), (547, 310), (548, 310), (549, 310), (548, 310), (548, 311), (548, 312), (548, 312), (548, 312), (548, 312), (548, 313), (547, 314), (546, 315), (547, 315), (547, 320), (547, 321), (547, 321), (547, 322), (547, 322), (545, 321), (547, 323), (547, 323), (545, 323), (548, 325), (545, 324), (548, 327), (546, 327), (548, 328), (547, 328), (549, 329), (549, 329), (550, 330), (547, 329), (547, 329), (547, 329), (552, 332), (551, 332), (552, 335), (552, 335), (553, 335), (553, 334), (552, 330), (549, 329), (550, 328), (549, 328), (552, 329), (554, 330), (552, 329), (547, 331), (554, 329), (551, 327), (553, 328), (554, 328), (553, 328), (553, 328), (553, 327), (554, 328), (553, 327), (551, 326), (552, 326), (553, 327), (554, 327), (554, 327), (552, 326), (554, 327), (552, 326), (554, 327), (554, 327), (554, 326), (554, 325), (554, 324), (554, 324), (554, 323), (551, 321), (553, 322), (548, 318), (551, 320), (548, 317), (551, 319), (550, 317), (550, 316), (549, 314), (550, 314), (550, 313), (550, 313), (551, 313), (551, 312), (551, 312), (551, 312)]
    mse = calculate_mse(ideal, detector.center_mass)
    assert mse < 10
