#!/usr/bin/env python    
# -*- coding: utf-8 -*- 

#
#  Copyright 2019 The FATE Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
################################################################################
#
#
################################################################################
from federatedml.util import consts


class DataIOParam(object):
    """
    Define dataio parameters that used in federated ml.

    Parameters
    ----------
    input_format : str, accepted 'dense','sparse' only in this version. default: 'dense'

    delimitor : str, the delimitor of data input, default: ','

    data_type : str, the data type of data input, accedted 'float','float64','int','int64','str','long'
               "default: "float64"

    missing_fill : bool, need to fill missing value or not, accepted only True/False, default: True

    default_value : object, accepted all python supported value type, will raise error if
                   type not consist with data_type, default: 0

    with_label : bool, True if input data consist of label, False otherwise. default: 'false'

    label_idx : int, accepted 'int','long' only, use when with_label is True. default: 'false'

    label_type : object, accepted 'int','int64','float','float64','long','str' only,
                use when with_label is True. default: 'false'

    output_format : str, accepted 'dense','sparse' only in this version. default: 'dense'

    """

    def __init__(self, input_format="dense", delimitor=',', data_type='float64',
                 missing_fill=True, default_value=0, with_label=False, label_idx=0,
                 label_type='int', output_format='dense'):
        self.input_format = input_format
        self.delimitor = delimitor
        self.data_type = data_type
        self.missing_fill = missing_fill
        self.default_value = default_value
        self.with_label = with_label
        self.label_idx = label_idx
        self.label_type = label_type
        self.output_format = output_format


class EncryptParam(object):
    """
    Define encryption method that used in federated ml.

    Parameters
    ----------
    method : str, default: 'Paillier'
        If method is 'Paillier', Paillier encryption will be used for federated ml.
        To use non-encryption version in HomoLR, just set this parameter to be any other str.
        For detail of Paillier encryption, please check out the paper mentioned in README file.

    key_length : int, default: 1024
        Used to specify the length of key in this encryption method. Only needed when method is 'Paillier'

    """

    def __init__(self, method=consts.PAILLIER, key_length=1024):
        self.method = method
        self.key_length = key_length


class EvaluateParam(object):
    """
    Define the evaluation method of binary/multiple classification and regression

    Parameters
    ----------
    metrics: A list of evaluate index. Support 'auc', 'ks', 'lift', 'precision' ,'recall' and 'accuracy', 'explain_variance',
            'mean_absolute_error', 'mean_squared_error', 'mean_squared_log_error','median_absolute_error','r2_score','root_mean_squared_error'.
            For example, metrics can be set as ['auc', 'precision', 'recall'], then the results of these indexes will be output.

    classi_type: string, support 'binary' for HomoLR, HeteroLR and Secureboosting. support 'regression' for Secureboosting. 'multi' is not support these version

    pos_label: specify positive label type, can be int, float and str, this depend on the data's label, this parameter effective only for 'binary'

    thresholds: A list of threshold. Specify the threshold use to separate positive and negative class. for example [0.1, 0.3,0.5], this parameter effective only for 'binary'
    """

    def __init__(self, metrics=None, classi_type="binary", pos_label=None, thresholds=None):
        self.metrics = metrics
        self.classi_type = classi_type
        self.pos_label = pos_label
        if thresholds is None:
            thresholds = [0.5]

        self.thresholds = thresholds


class ObjectiveParam(object):
    """
    Define objective parameters that used in federated ml.

    Parameters
    ----------
    objective : None or str, accepted None,'cross_entropy','lse','lae','log_cosh','tweedie','fair','huber' only,
                None in host's config, should be str in guest'config.
                when task_type is classification, only support cross_enctropy,
                other 6 types support in regression task. default: None

    params : None or list, should be non empty list when objective is 'tweedie','fair','huber',
             first element of list shoulf be a float-number large than 0.0 when objective is 'fair','huber',
             first element of list should be a float-number in [1.0, 2.0) when objective is 'tweedie'
    """

    def __init__(self, objective=None, params=None):
        self.objective = objective
        self.params = params


class PredictParam(object):
    """
    Define the predict method of HomoLR, HeteroLR, SecureBoosting

    Parameters
    ----------
    with_proba: Boolean, Specify whether the result contains probability

    threshold: float or int, The threshold use to separate positive and negative class. Normally, it should be (0,1)
    """

    def __init__(self, with_proba=True, threshold=0.5):
        self.with_proba = with_proba
        self.threshold = threshold


class WorkFlowParam(object):
    """
    Define Workflow parameters used in federated ml.

    Parameters
    ----------
    method : str, 'train', 'predict', 'intersect' or 'cross_validation'. default: 'train'
        The working method of this task.

    train_input_table : str, default: None
        Required when method is 'train'. Specify the table name of input data in database.

    train_input_namespace : str, default: None
        Required when method is 'train'. Specify the namespace of input data in database.

    model_table : str, default: None
        Required when method is 'train', 'predict' or 'cross_validation'.
        Specify the table name to save or load model. When method is 'train' or 'cross_validation', this parameter
        is used to save model. When method is predict, it is used to load model.

    model_namespace : str, default: None
        Required when method is 'train', 'predict' or 'cross_validation'.
        Specify the namespace to save or load model. When method is 'train' or 'cross_validation', this parameter
        is used to save model. When method is predict, it is used to load model.

    predict_input_table : str, default: None
        Required when method is 'predict'. Specify the table name of predict input data.

    predict_input_namespace : str, default: None
        Required when method is 'predict'. Specify the namespace of predict input data in database.

    predict_result_partition : int, default: 1
        The partition number used for predict result.

    predict_output_table : str, default: None
        Required when method is 'predict'. Specify the table name of predict output data.

    predict_output_namespace : str, default: None
        Required when method is 'predict'. Specify the namespace of predict output data in database.

    evaluation_output_table : str, default: None
        Required when method is 'train', 'predict' or 'cross_validation'.
         Specify the table name of evalation output data.

    evaluation_output_namespace : str, default: None
        Required when method is 'train', 'predict' or 'cross_validation'.
         Specify the namespace of predict output data in database.

    data_input_table : str, defalut: None
        Required when method is 'cross_validation'. Specify the table name of input data.

    data_input_namespace : str, defalut: None
        Required when method is 'cross_validation'. Specify the namespace of input data.

    intersect_data_output_table : str, defalut: None
        Required when method is 'intersect'. Specify the table name of output data.

    intersect_data_output_namespace : str, defalut: None
        Required when method is 'intersect'. Specify the namespace of output data.

    do_cross_validation : Abandonded.

    work_mode: int, 0 or 1. default: 0
        Specify the work mode. 0 means standalone version, 1 represent for cluster version.

    n_splits: int, default: 5
        The number of fold used in KFold validation. It is required in 'cross_validation' only.

    need_intersect: bool, default: True
        Whether this task need to do intersect. No need to specify in Homo task.

    """

    def __init__(self, method='train', train_input_table=None, train_input_namespace=None, model_table=None,
                 model_namespace=None, predict_input_table=None, predict_input_namespace=None,
                 predict_result_partition=1, predict_output_table=None, predict_output_namespace=None,
                 evaluation_output_table=None, evaluation_output_namespace=None,
                 data_input_table=None, data_input_namespace=None, intersect_data_output_table=None,
                 intersect_data_output_namespace=None, dataio_param=DataIOParam(), predict_param=PredictParam(),
                 evaluate_param=EvaluateParam(), do_cross_validation=False, work_mode=0,
                 n_splits=5, need_intersect=True):
        self.method = method
        self.train_input_table = train_input_table
        self.train_input_namespace = train_input_namespace
        self.model_table = model_table
        self.model_namespace = model_namespace
        self.predict_input_table = predict_input_table
        self.predict_input_namespace = predict_input_namespace
        self.predict_output_table = predict_output_table
        self.predict_output_namespace = predict_output_namespace
        self.predict_result_partition = predict_result_partition
        self.evaluation_output_table = evaluation_output_table
        self.evaluation_output_namespace = evaluation_output_namespace
        self.data_input_table = data_input_table
        self.data_input_namespace = data_input_namespace
        self.intersect_data_output_table = intersect_data_output_table
        self.intersect_data_output_namespace = intersect_data_output_namespace
        self.dataio_param = dataio_param
        self.do_cross_validation = do_cross_validation
        self.n_splits = n_splits
        self.work_mode = work_mode
        self.predict_param = predict_param
        self.evaluate_param = evaluate_param
        self.need_intersect = need_intersect


class InitParam(object):
    """
    Initialize Parameters used in initializing a model.

    Parameters
    ----------
    init_method : str, 'random_uniform', 'random_normal', 'ones', 'zeros' or 'const'. default: 'random_uniform'
        Initial method.

    init_const : int or float, default: 1
        Required when init_method is 'const'. Specify the constant.

    fit_intercept : bool, default: True
        Whether to initialize the intercept or not.

    """

    def __init__(self, init_method='random_uniform', init_const=1, fit_intercept=True):
        self.init_method = init_method
        self.init_const = init_const
        self.fit_intercept = fit_intercept


class EncodeParam(object):
    """
    Define the encode method

    Parameters
    ----------
    salt: the src data string will be str = str + salt, default by empty string

    encode_method: str, the encode method of src data string, it support md5, sha1, sha224, sha256, sha384, sha512, default by None

    base64: boolean, if True, the result of encode will be changed to base64, default by False
    """

    def __init__(self, salt='', encode_method='none', base64=False):
        self.salt = salt
        self.encode_method = encode_method
        self.base64 = base64


class IntersectParam(object):
    """
    Define the intersect method

    Parameters
    ----------
    intersect_method: str, it supports 'rsa' and 'raw', default by 'raw'

    random_bit: positive int, it will define the encrypt length of rsa algorithm. It effective only for intersect_method is rsa

    is_send_intersect_ids: boolean. In rsa, 'is_send_intersect_ids' is True means guest will send intersect results to host, and False will not.
                            while in raw, 'is_send_intersect_ids' is True means the role of "join_role" will send intersect results and the other will get them.
                            Default by True.

    is_get_intersect_ids: boolean, In rsa, it will get the results from other. It effective only for rsa and only be True will other's 'is_send_intersect_ids' is True.Default by True

    join_role: str, it supports "guest" and "host" only and effective only for raw. If it is "guest", the host will send its ids to guest and find the intersection of
                ids in guest; if it is "host", the guest will send its ids. Default by "guest".

    with_encode: boolean, if True, it will use encode method for intersect ids. It effective only for "raw".

    encode_params: EncodeParam, it effective only for with_encode is True
    """

    def __init__(self, intersect_method=consts.RAW, random_bit=128, is_send_intersect_ids=True,
                 is_get_intersect_ids=True, join_role="guest", with_encode=False, encode_params=EncodeParam()):
        self.intersect_method = intersect_method
        self.random_bit = random_bit
        self.is_send_intersect_ids = is_send_intersect_ids
        self.is_get_intersect_ids = is_get_intersect_ids
        self.join_role = join_role
        self.with_encode = with_encode
        self.encode_params = encode_params


class LogisticParam(object):
    """
    Parameters used for Logistic Regression both for Homo mode or Hetero mode.

    Parameters
    ----------
    penalty : str, 'L1' or 'L2'. default: 'L2'
        Penalty method used in LR. Please note that, when using encrypted version in HomoLR,
        'L1' is not supported.

    eps : float, default: 1e-5
        The tolerance of convergence

    alpha : float, default: 1.0
        Regularization strength coefficient.

    optimizer : str, 'sgd', 'rmsprop', 'adam' or 'adagrad', default: 'sgd'
        Optimize method

    party_weight : int or float, default: 1
        Required in Homo LR. Setting the weight of model updated for this party.
        The higher weight set, the higher influence made for this party when updating model.

    batch_size : int, default: -1
        Batch size when updating model. -1 means use all data in a batch. i.e. Not to use mini-batch strategy.

    learning_rate : float, default: 0.01
        Learning rate

    max_iter : int, default: 100
        The maximum iteration for training.

    converge_func : str, 'diff' or 'abs', default: 'diff'
        Method used to judge converge or not.
            a)	diff： Use difference of loss between two iterations to judge whether converge.
            b)	abs: Use the absolute value of loss to judge whether converge.

    re_encrypt_batches : int, default: 2
        Required when using encrypted version HomoLR. Since multiple batch updating coefficient may cause
        overflow error. The model need to be re-encrypt for every several batches. Please be careful when setting
        this parameter. Too large batches may cause training failure.

    model_path : Abandoned

    table_name : Abandoned

    """

    def __init__(self, penalty='L2',
                 eps=1e-5, alpha=1.0, optimizer='sgd', party_weight=1,
                 batch_size=-1, learning_rate=0.01, init_param=InitParam(),
                 max_iter=100, converge_func='diff',
                 encrypt_param=EncryptParam(), re_encrypt_batches=2,
                 model_path='lr_model', table_name='lr_table'):
        self.penalty = penalty
        self.eps = eps
        self.alpha = alpha
        self.optimizer = optimizer
        self.batch_size = batch_size
        self.learning_rate = learning_rate
        self.init_param = init_param
        self.max_iter = max_iter
        self.converge_func = converge_func
        self.encrypt_param = encrypt_param
        self.re_encrypt_batches = re_encrypt_batches
        self.model_path = model_path
        self.table_name = table_name
        self.party_weight = party_weight


class DecisionTreeParam(object):
    """
    Define dataio parameters that used in federated ml.

    Parameters
    ----------
    criterion_method : str, accepted "xgboost" only, the criterion function to use, default: 'xgboost'

    criterion_params: list, should be non empty and first element is float-number, default: 0.1.

    max_depth: int, positive integer, the max depth of a decision tree, default: 5

    min_sample_split: int, least quantity of nodes to split, default: 2

    min_impurity_split: float, least gain of a single split need to reach, default: 1e-3

    min_leaf_node: int, when samples no more than min_leaf_node, it becomes a leave, default: 1

    max_split_nodes: int, positive integer, we will use no more than max_split_nodes to
                      parallel finding their splits in a batch, for memory consideration. default is 65536

    n_iter_no_change: bool, accepted True,False only, if set to True, tol will use to consider
                      stop tree growth. default: True

    tol: float, only use when n_iter_no_change is set to True, default: 0.001
    """

    def __init__(self, criterion_method="xgboost", criterion_params=[0.1], max_depth=5,
                 min_sample_split=2, min_imputiry_split=1e-3, min_leaf_node=1,
                 max_split_nodes=consts.MAX_SPLIT_NODES, n_iter_no_change=True, tol=0.001):
        self.criterion_method = criterion_method
        self.criterion_params = criterion_params
        self.max_depth = max_depth
        self.min_sample_split = min_sample_split
        self.min_impurity_split = min_imputiry_split
        self.min_leaf_node = min_leaf_node
        self.max_split_nodes = max_split_nodes
        self.n_iter_no_change = n_iter_no_change
        self.tol = tol


class BoostingTreeParam(object):
    """
    Define dataio parameters that used in federated ml.

    Parameters
    ----------
    task_type : str, accepted 'classification', 'regression' only, default: 'classification'

    tree_param : DecisionTreeParam Object, default: DecisionTreeParam()

    objective_param : ObjectiveParam Object, default: ObjectiveParam()

    learning_rate : float, accepted float, int or long only, the learning rate of secure boost. default: 0.3

    num_trees : int, accepted int, float only, the max number of trees to build. default: 5

    subsample_feature_rate : float, a float-number in [0, 1], default: 0.8

    n_iter_no_change : bool,
        when True and residual error less than tol, tree building process will stop. default: True

    encrypt_param : EncodeParam Object, encrypt method use in secure boost, default: EncryptParam()

    quantile_method : str, accepted 'bin_by_sample_data' or 'bin_by_data_block' only,
                      the quantile method use in secureboost, default: 'bin_by_sample_data'

    bin_num: int, positive integer greater than 1, bin number use in quantile. default: 32

    bin_gap: float, least difference between bin points, default: 1e-3

    bin_sample_num: int, if quantile method is 'bin_by_sample_data', max amount of samples to find bins.
                    default: 10000
    """

    def __init__(self, tree_param=DecisionTreeParam(), task_type=consts.CLASSIFICATION,
                 objective_param=ObjectiveParam(),
                 learning_rate=0.3, num_trees=5, subsample_feature_rate=0.8, n_iter_no_change=True,
                 tol=0.0001, encrypt_param=EncryptParam(), quantile_method="bin_by_sample_data",
                 bin_num=32, bin_gap=1e-3, bin_sample_num=10000):
        self.tree_param = tree_param
        self.task_type = task_type
        self.objective_param = objective_param
        self.learning_rate = learning_rate
        self.num_trees = num_trees
        self.subsample_feature_rate = subsample_feature_rate
        self.n_iter_no_change = n_iter_no_change
        self.tol = tol
        self.encrypt_param = encrypt_param
        self.quantile_method = quantile_method
        self.bin_num = bin_num
        self.bin_gap = bin_gap
        self.bin_sample_num = bin_sample_num


class FTLModelParam(object):
    """
    Defines parameters for FTL model

    Parameters
    ----------
    max_iteration: integer, default: 10
        The number of passes over the training data (aka epochs), must be positive integer

    eps: numeric, default: 1e-3
        The converge threshold, must be positive number

    alpha: numeric, default: 100
        The weight for objective function loss, must be positive number

    is_encrypt: bool, default; True
        The indicator indicating whether we use encrypted version of ftl or plain version, must be bool

    enc_ftl: str default "dct_enc_ftl"
        The name for encrypted federated transfer learning algorithm

    """

    def __init__(self, max_iteration=10, batch_size=64, eps=1e-5,
                 alpha=100, lr_decay=0.001, l2_para=1, is_encrypt=True, enc_ftl="dct_enc_ftl"):
        self.max_iter = max_iteration
        self.batch_size = batch_size
        self.eps = eps
        self.alpha = alpha
        self.lr_decay = lr_decay
        self.l2_para = l2_para
        self.is_encrypt = is_encrypt
        self.enc_ftl = enc_ftl


class LocalModelParam(object):
    """
    Defines parameters for FTL model

    Parameters
    ----------
    input_dim: integer, default: None
        The dimension of input samples, must be positive integer

    encode_dim: integer, default: 5
        The dimension of the encoded representation of input samples, must be positive integer

    learning_rate: float, default: 0.001
        The learning rate for training model, must between 0 and 1 exclusively


    """

    def __init__(self, input_dim=None, encode_dim=5, learning_rate=0.001):
        self.input_dim = input_dim
        self.encode_dim = encode_dim
        self.learning_rate = learning_rate


class FTLDataParam(object):
    """
    Defines parameters for FTL data model

    Parameters
    ----------
    file_path: str, default: None
        The file path to FTL data configuration JSON file, must be string or None

    n_feature_guest: integer, default: 10
        The number of features at guest side, must be positive integer

    n_feature_host: integer, default: 23
        The number of features at host side, must be positive integer

    overlap_ratio: float, default: 0.1
        The ratio of overlapping samples between guest and host, must between 0 and 1 exclusively

    guest_split_ratio: float, default: 0.9
        The ratio of number of samples excluding overlapping samples at guest side, must between 0 and 1 exclusively

    num_samples: numeric, default: None
        The total number of samples used for train/validation/test, must be positive integer or None. If None, all samples
        would be used.

    balanced: bool, default; True
        The indicator indicating whether balance samples, must be bool

    is_read_table: bool, default; False
        The indicator indicating whether read data from dtable, must be bool

    """

    def __init__(self, file_path=None, n_feature_guest=10, n_feature_host=23, overlap_ratio=0.1, guest_split_ratio=0.9,
                 num_samples=None, balanced=True, is_read_table=False):
        self.file_path = file_path
        self.n_feature_guest = n_feature_guest
        self.n_feature_host = n_feature_host
        self.overlap_ratio = overlap_ratio
        self.guest_split_ratio = guest_split_ratio
        self.num_samples = num_samples
        self.balanced = balanced
        self.is_read_table = is_read_table


class FTLValidDataParam(object):
    """
    Defines parameters for FTL validation data model

    Parameters
    ----------
    file_path: str, default: None
        The file path to FTL data configuration JSON file, must be string or None

    num_samples: numeric, default: None
        The total number of samples used for validation, must be positive integer or None. If None, all samples
        would be used.

    is_read_table: bool, default; False
        The indicator indicating whether read data from dtable, must be bool

    """
    def __init__(self, file_path=None, num_samples=None, is_read_table=False):
        self.file_path = file_path
        self.num_samples = num_samples
        self.is_read_table = is_read_table


class FeatureBinningParam(object):
    """
    Define the feature binning method

    Parameters
    ----------
    process_method : str, 'fit' or 'transform', default: "fit"
        Specify what process to do.

    method : str, 'quantile', default: 'quantile'
        Binning method.

    compress_thres: int, default: 10000
        When the number of saved summaries exceed this threshold, it will call its compress function

    head_size: int, default: 10000
        The buffer size to store inserted observations. When head list reach this buffer size, the
        QuantileSummaries object start to generate summary(or stats) and insert into its sampled list.

    error: float, 0 <= error < 1 default: 0.001
        The error of tolerance of binning. The final split point comes from original data, and the rank
        of this value is close to the exact rank. More precisely,
        floor((p - 2 * error) * N) <= rank(x) <= ceil((p + 2 * error) * N)
        where p is the quantile in float, and N is total number of data.

    bin_num: int, bin_num > 0, default: 10
        The max bin number for binning

    cols : list or int, default: -1
        Specify which columns need to calculated. -1 represent for all columns

    adjustment_factor : float, default: 0.5
        the adjustment factor when calculating WOE. This is useful when there is no event or non-event in
        a bin.

    local_only : bool, default: False
        Whether just provide binning method to guest party. If true, host party will do nothing.

    result_table : str, default: 'binning_table'
        Table name to save result

    result_namespace : str, default: 'binning_namespace'
        Namespace to save result

    display_result : list, default: ['iv']
        Specify what results to show. The available results include:
        ['iv', 'woe_array', 'iv_array', 'event_count_array', 'non_event_count_array', 'event_rate_array',
        'non_event_rate_array', 'is_woe_monotonic', 'bin_nums', 'split_points']
        for each features

    """

    def __init__(self, process_method='fit',
                 method=consts.QUANTILE, compress_thres=consts.DEFAULT_COMPRESS_THRESHOLD,
                 head_size=consts.DEFAULT_HEAD_SIZE,
                 error=consts.DEFAULT_RELATIVE_ERROR,
                 bin_num=consts.G_BIN_NUM, cols=-1, adjustment_factor=0.5,
                 local_only=False,
                 result_table='binning_table',
                 result_namespace='binning_namespace',
                 display_result='simple'):
        self.process_method = process_method
        self.method = method
        self.compress_thres = compress_thres
        self.head_size = head_size
        self.error = error
        self.adjustment_factor = adjustment_factor
        self.bin_num = bin_num
        self.cols = cols
        self.local_only = local_only
        self.result_table = result_table
        self.result_namespace = result_namespace

        if display_result == 'simple':
            display_result = ['iv']
        self.display_result = display_result


class UniqueValueParam(object):
    """
    Use the difference between max-value and min-value to judge.

    Parameters
    ----------
    eps: float, default: 1e-5
        The column(s) will be filtered if its difference is smaller than eps.
    """

    def __init__(self, eps=1e-5):
        self.eps = eps


class IVSelectionParam(object):
    """
    Use information values to select features.

    Parameters
    ----------
    value_threshold: float, default: 1.0
        Used if iv_value_thres method is used in feature selection.

    percentile_threshold: float, 0 <= percentile_threshold <= 1.0, default: 1.0
        Percentile threshold for iv_percentile method

    """

    def __init__(self, value_threshold=1.0, percentile_threshold=1.0, bin_param=FeatureBinningParam()):
        self.value_threshold = value_threshold
        self.percentile_threshold = percentile_threshold
        self.bin_param = bin_param


class CoeffOfVarSelectionParam(object):
    """
    Use coefficient of variation to select features. When judging, the absolute value will be used.

    Parameters
    ----------
    value_threshold: float, default: 1.0
        Used if coefficient_of_variation_value_thres method is used in feature selection.

    percentile_threshold: float, 0 <= percentile_threshold <= 1.0, default: 1.0
        Percentile threshold for coefficient_of_variation_percentile method

    """

    def __init__(self, value_threshold=1.0):
        self.value_threshold = value_threshold


class OutlierColsSelectionParam(object):
    """
    Given percentile and threshold. Judge if this quantile point is larger than threshold. Filter those larger ones.

    Parameters
    ----------
    percentile: float, [0., 1.] default: 1.0
        The percentile points to compare.

    upper_threshold: float, default: 1.0
        Percentile threshold for coefficient_of_variation_percentile method

    """

    def __init__(self, percentile=1.0, upper_threshold=1.0):
        self.percentile = percentile
        self.upper_threshold = upper_threshold


class FeatureSelectionParam(object):
    """
    Define the feature selection parameters.

    Parameters
    ----------
    method : str, 'fit', 'transform' or 'fit_transform', default: 'fit'
        Decide what process to do.

    select_cols: list or int, default: -1
        Specify which columns need to calculated. -1 represent for all columns.

    filter_method: list, default: ["unique_value", "iv_value_thres", "iv_percentile",
                "coefficient_of_variation_value_thres", "outlier_cols"]

        Specify the filter methods used in feature selection. The orders of filter used is depended on this list.
        Please be notified that, if a percentile method is used after some certain filter method,
        the percentile represent for the ratio of rest features.
        e.g. If you have 10 features at the beginning. After first filter method, you have 8 rest. Then, you want
        top 80% highest iv feature. Here, we will choose floor(0.8 * 8) = 6 features instead of 8.

        unique_value: filter the columns if all values in this feature is the same

        iv_value_thres: Use information value to filter columns. If this method is set, a float threshold need to be provided.
            Filter those columns whose iv is smaller than threshold.

        iv_percentile: Use information value to filter columns. If this method is set, a float ratio threshold
            need to be provided. Pick floor(ratio * feature_num) features with higher iv.

        coefficient_of_variation_value_thres: Use coefficient of variation to judge whether filtered or not.

        coefficient_of_variation_percentile: Pick floor(ratio * feature_num) features with higher coefficient of
                                variation (which means filter the rest)

        outlier_cols: Filter columns whose certain percentile value is larger than a threshold.


    """

    def __init__(self, method='fit', select_cols=-1, filter_method=None, local_only=False,
                 unique_param=UniqueValueParam(),
                 iv_param=IVSelectionParam(), coe_param=CoeffOfVarSelectionParam(),
                 outlier_param=OutlierColsSelectionParam(), bin_param=FeatureBinningParam(),
                 result_table='binning_table',
                 result_namespace='binning_namespace',
                 ):
        self.method = method
        self.select_cols = select_cols
        if filter_method is None:
            self.filter_method = [consts.UNIQUE_VALUE]
        else:
            self.filter_method = filter_method

        self.local_only = local_only
        self.unique_param = unique_param
        self.iv_param = iv_param
        self.coe_param = coe_param
        self.outlier_param = outlier_param
        self.bin_param = bin_param
        self.result_table = result_table
        self.result_namespace = result_namespace
