import numpy as np
from array import array
from skmultiflow.data.generators.random_tree_generator import RandomTreeGenerator
from skmultiflow.classification.trees.hoeffding_tree import HoeffdingTree


def test_hoeffding_tree():
    stream = RandomTreeGenerator(tree_random_state=23, sample_random_state=12, n_classes=4, n_cat_features=2,
                                 n_num_features=5, n_categories_per_cat_feature=5, max_tree_depth=6, min_leaf_depth=3,
                                 fraction_leaves_per_level=0.15)
    stream.prepare_for_use()

    nominal_attr_idx = [x for x in range(5, stream.n_features)]
    learner = HoeffdingTree(nominal_attributes=nominal_attr_idx)

    cnt = 0
    max_samples = 5000
    predictions = array('d')
    proba_predictions = []
    wait_samples = 100

    while cnt < max_samples:
        X, y = stream.next_sample()
        # Test every n samples
        if cnt % wait_samples == 0:
            predictions.append(learner.predict(X)[0])
            proba_predictions.append(learner.predict_proba(X)[0])
        learner.partial_fit(X, y)
        cnt += 1

    expected_predictions = array('d', [0.0, 0.0, 1.0, 3.0, 0.0, 0.0, 3.0, 0.0, 1.0, 1.0,
                                       2.0, 0.0, 2.0, 1.0, 1.0, 2.0, 1.0, 3.0, 0.0, 1.0,
                                       1.0, 1.0, 1.0, 0.0, 3.0, 1.0, 2.0, 1.0, 1.0, 3.0,
                                       2.0, 1.0, 2.0, 2.0, 2.0, 1.0, 1.0, 1.0, 0.0, 1.0,
                                       2.0, 0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 1.0, 3.0, 2.0])

    expected_proba_predictions_0 = [[0],
                                  [0.4497009191972877, 0.37095206116508905, 0.009627766164113276, 0.16971925347350986],
                                  [0.12062048832967867, 0.4935697059828874, 0.3434983254040227, 0.04231148028341116],
                                  [0.04364722810617002, 0.4189877314198612, 0.08110309979616029, 0.4562619406778085],
                                  [0.4344104787306036, 0.3299995063591682, 0.024089989360482997, 0.21150002554974515],
                                  [0.7374142716167381, 0.16285656920282202, 0.03792060836165301, 0.06180855081878693],
                                  [0.10908688012860641, 0.2776317827217744, 0.2238168713539179, 0.3894644657957014],
                                  [0.720493928676314, 0.058663966762511274, 0.15168590932103787, 0.06915619524013679],
                                  [0.11056810243207303, 0.5936874357275022, 0.15196987660273503, 0.14377458523768974],
                                  [0.18632734990183897, 0.6561741972054181, 0.016917638551037492, 0.14058081434170533],
                                  [0.2545569777793396, 0.1623959823557714, 0.48274673321416545, 0.10030030665072365],
                                  [0.7148334953691984, 0.07562549988498361, 0.09080525831716496, 0.11873574642865306],
                                  [0.1577184124576196, 0.2487034908865402, 0.5517935839142933, 0.041784512741546806],
                                  [0.1213337064672237, 0.3855096079248308, 0.2813096697401397, 0.21184701586780594],
                                  [0.18033023016655259, 0.49015140622118003, 0.25643923732277335, 0.07307912628949402],
                                  [0.22601491532970522, 0.28975299020226924, 0.41073395499025306, 0.0734981394777724],
                                  [0.2506876589492564, 0.5427177325169206, 0.07773473212020429, 0.1288598764136188],
                                  [0.09367683972517342, 0.24005968591840493, 0.24167955530476296, 0.42458391905165876],
                                  [0.5166985737497305, 0.10976508286174581, 0.08639954675987715, 0.28713679662864644],
                                  [0.1037490207681112, 0.507944216814439, 0.16554905245416293, 0.22275770996328687],
                                  [0.2732707106008795, 0.4052665174756578, 0.15164125572436063, 0.1698215161991021],
                                  [0.1057193955648248, 0.49566572923927954, 0.2028121086864112, 0.1958027665094845],
                                  [0.18048075889450155, 0.4284621655229268, 0.01585775226508467, 0.375199323317487],
                                  [0.4454914207088857, 0.17885604560834226, 0.3025076244476781, 0.07314490923509392],
                                  [0.08709233862702367, 0.19847514189348278, 0.3051425507259399, 0.40928996875355356],
                                  [0.05465067622610323, 0.5578423202372196, 0.20904918506809625, 0.17845781846858094],
                                  [0.05841820433386879, 0.22380040998298723, 0.4706020103897857, 0.24717937529335818],
                                  [0.1597232504007311, 0.4322477786748696, 0.2710997594814109, 0.13692921144298836],
                                  [0.08881096542969866, 0.5285443592930786, 0.1940462989077328,  0.18859837636948978],
                                  [0.2640456286534356, 0.3089545751540895,  0.017476708608517456, 0.40952308758395745],
                                  [0.20067601265352422, 0.25438074134609345,  0.45503249454689093, 0.08991075145349145],
                                  [0.25185790918136547, 0.5148886009467156, 0.08016443128346412, 0.15308905858845478],
                                  [0.16920513681025356, 0.34048425737030813, 0.41602879501239426, 0.07428181080704413],
                                  [0.21858277288226355, 0.15685198795268473, 0.4882158794592465, 0.13634935970580517],
                                  [0.2242212376087198, 0.18777251540668483, 0.3968100248934075, 0.19119622209118795],
                                  [0.3140746185947891, 0.3962193786016646, 0.08288080280398603, 0.20682519999956034],
                                  [0.15936796672093206, 0.6645518615993655, 0.04416189851044389, 0.13191827316925842],
                                  [0.3104821907510398, 0.4249560358876497, 0.14986989268115317, 0.11469188068015747],
                                  [0.4263166916129654, 0.2839916481792985, 0.11102252073286453, 0.17866913947487156],
                                  [0.3085346179247346, 0.4860297153761375, 0.12464253600354598, 0.08079313069558215],
                                  [0.11455590802395119,  0.3063082189456146,  0.3296272507912796, 0.24950862223915465],
                                  [0.41042156141864433, 0.3168863524888606, 0.2350957318452348, 0.0375963542472604],
                                  [0.2965517426024982, 0.14680659530523144, 0.3580427821705787, 0.19859887992169165],
                                  [0.5588896290518159, 0.11059312473837576, 0.09839164179782577, 0.2321256044119825],
                                  [0.4320393215429663, 0.14292789756628382, 0.2655069962848666, 0.15952578460588332],
                                  [0.4179261534312665, 0.2883958448486473, 0.0685538639026241, 0.2251241378174621],
                                  [0.45460381788974635, 0.1179106446843459, 0.23629901454221744,  0.19118652288369026],
                                  [0.2424354415168287, 0.4791854372180899, 0.23820608169386026, 0.040173039571221036],
                                  [0.06639710430396381, 0.20099823750215168, 0.25521994411302296, 0.4773847140808615],
                                  [0.18036776034892207, 0.2567511371264665, 0.3043615398596443, 0.2585195626649672]]

    expected_proba_predictions_1 = [[0],
                                  [0.4497009191972878, 0.3709520611650891, 0.009627766164113278, 0.16971925347350988],
                                  [0.12062048832967867, 0.4935697059828874, 0.3434983254040227, 0.04231148028341116],
                                  [0.04364722810617002, 0.4189877314198612, 0.08110309979616029, 0.4562619406778085],
                                  [0.4344104787306036, 0.3299995063591682, 0.024089989360482997, 0.21150002554974515],
                                  [0.7374142716167381, 0.16285656920282202, 0.03792060836165301, 0.06180855081878693],
                                  [0.1090868801286064, 0.27763178272177436, 0.22381687135391784, 0.3894644657957013],
                                  [0.720493928676314, 0.058663966762511274, 0.15168590932103787, 0.06915619524013679],
                                  [0.11056810243207303, 0.5936874357275022, 0.15196987660273503, 0.14377458523768974],
                                  [0.18632734990183897, 0.6561741972054181, 0.016917638551037492, 0.14058081434170533],
                                  [0.2545569777793396, 0.1623959823557714, 0.48274673321416545, 0.10030030665072365],
                                  [0.7148334953691983, 0.0756254998849836, 0.09080525831716495, 0.11873574642865305],
                                  [0.15771841245761964, 0.24870349088654023, 0.5517935839142935, 0.04178451274154681],
                                  [0.12133370646722368, 0.3855096079248307, 0.2813096697401396, 0.21184701586780588],
                                  [0.18033023016655259, 0.49015140622118003, 0.25643923732277335, 0.07307912628949402],
                                  [0.22601491532970522, 0.28975299020226924, 0.41073395499025306, 0.0734981394777724],
                                  [0.2506876589492564, 0.5427177325169206, 0.07773473212020429, 0.1288598764136188],
                                  [0.09367683972517342, 0.24005968591840493, 0.24167955530476296, 0.42458391905165876],
                                  [0.5166985737497305, 0.10976508286174581, 0.08639954675987715, 0.28713679662864644],
                                  [0.1037490207681112, 0.507944216814439, 0.16554905245416293, 0.22275770996328687],
                                  [0.2732707106008795, 0.4052665174756578, 0.15164125572436063, 0.1698215161991021],
                                  [0.1057193955648248, 0.49566572923927954, 0.2028121086864112, 0.1958027665094845],
                                  [0.18048075889450155, 0.4284621655229268, 0.01585775226508467, 0.375199323317487],
                                  [0.4454914207088857, 0.17885604560834226, 0.3025076244476781, 0.07314490923509392],
                                  [0.08709233862702367, 0.19847514189348278, 0.3051425507259399, 0.40928996875355356],
                                  [0.05465067622610323, 0.5578423202372196, 0.20904918506809625, 0.17845781846858094],
                                  [0.05841820433386879, 0.22380040998298723, 0.4706020103897857, 0.24717937529335818],
                                  [0.15972325040073113, 0.43224777867486963, 0.27109975948141096, 0.13692921144298836],
                                  [0.08881096542969866, 0.5285443592930786, 0.1940462989077328, 0.18859837636948978],
                                  [0.2640456286534356, 0.3089545751540895, 0.017476708608517456, 0.40952308758395745],
                                  [0.20067601265352422, 0.25438074134609345, 0.45503249454689093, 0.08991075145349145],
                                  [0.25185790918136547, 0.5148886009467156, 0.08016443128346412, 0.15308905858845478],
                                  [0.16920513681025356, 0.34048425737030813, 0.41602879501239426, 0.07428181080704413],
                                  [0.21858277288226355, 0.15685198795268473, 0.4882158794592465, 0.13634935970580517],
                                  [0.2242212376087198, 0.18777251540668483, 0.3968100248934075, 0.19119622209118795],
                                  [0.3140746185947891, 0.3962193786016646, 0.08288080280398603, 0.20682519999956034],
                                  [0.15936796672093206, 0.6645518615993655, 0.04416189851044389, 0.13191827316925842],
                                  [0.3104821907510398, 0.4249560358876497, 0.14986989268115317, 0.11469188068015747],
                                  [0.4263166916129654, 0.2839916481792985, 0.11102252073286453, 0.17866913947487156],
                                  [0.3085346179247345, 0.48602971537613743, 0.12464253600354595, 0.08079313069558215],
                                  [0.11455590802395119, 0.3063082189456146, 0.3296272507912796, 0.24950862223915465],
                                  [0.41042156141864433, 0.3168863524888606, 0.2350957318452348, 0.0375963542472604],
                                  [0.2965517426024982, 0.14680659530523144, 0.3580427821705787, 0.19859887992169165],
                                  [0.5588896290518159, 0.11059312473837576, 0.09839164179782577, 0.2321256044119825],
                                  [0.43203932154296626, 0.1429278975662838, 0.2655069962848666, 0.1595257846058833],
                                  [0.41792615343126654, 0.28839584484864733, 0.0685538639026241, 0.22512413781746213],
                                  [0.45460381788974635, 0.1179106446843459, 0.23629901454221744, 0.19118652288369026],
                                  [0.24243544151682872, 0.47918543721809, 0.2382060816938603, 0.04017303957122104],
                                  [0.06639710430396381, 0.20099823750215168, 0.25521994411302296, 0.4773847140808615],
                                  [0.18036776034892207, 0.2567511371264665, 0.3043615398596443, 0.2585195626649672]]

    np.alltrue(proba_predictions == expected_proba_predictions_0)

    assert np.alltrue(proba_predictions == expected_proba_predictions_0) or \
           np.alltrue(proba_predictions == expected_proba_predictions_1)
    assert np.alltrue(predictions == expected_predictions)

    expected_info = 'HoeffdingTree: max_byte_size: 33554432 - memory_estimate_period: 1000000 - grace_period: 200 ' \
                    '- split_criterion: info_gain - split_confidence: 1e-07 - tie_threshold: 0.05 ' \
                    '- binary_split: False - stop_mem_management: False - remove_poor_atts: False ' \
                    '- no_pre_prune: False - leaf_prediction: nba - nb_threshold: 0 - nominal_attributes: [5, 6, 7,' \
                    ' 8, 9, 10, 11, 12, 13, 14] - '
    assert learner.get_info() == expected_info

    expected_model_1 = 'Leaf = Class 1.0 | {0.0: 1423.0, 1.0: 1745.0, 2.0: 978.0, 3.0: 854.0}\n'
    expected_model_2 = 'Leaf = Class 1.0 | {1.0: 1745.0, 2.0: 978.0, 0.0: 1423.0, 3.0: 854.0}\n'
    assert (learner.get_model_description() == expected_model_1) \
           or (learner.get_model_description() == expected_model_2)