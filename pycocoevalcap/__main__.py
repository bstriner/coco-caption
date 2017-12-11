import argparse
import json
from json import encoder

from pycocoevalcap.eval import COCOEvalCap
from pycocotools.coco import COCO

encoder.FLOAT_REPR = lambda o: format(o, '.3f')


def evaluate_captions(
        annotation_file,
        results_file,
        eval_file,
        eval_images_file):
    """

    :param annotation_file:
    :param results_file:
    :param eval_file:
    :param eval_images_file:
    :return:
    """
    coco = COCO(annotation_file)
    coco_res = coco.loadRes(results_file)
    coco_eval = COCOEvalCap(coco, coco_res)
    coco_eval.params['image_id'] = coco_res.getImgIds()
    coco_eval.evaluate()
    for metric, score in coco_eval.eval.items():
        print('{}: {:.03f}'.format(metric, score))
    with open(eval_images_file, 'w') as f:
        json.dump(coco_eval.evalImgs, f)
    with open(eval_file, 'w') as f:
        json.dump(coco_eval.eval, f)


def main(args=None):
    """The main routine."""
    # if args is None:
    #    args = sys.argv[1:]
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "annotation-file",
        type=str,
        help="Annotation file (e.g., captions_val2017.json)")
    parser.add_argument(
        "results-file",
        type=str,
        help="Results file")
    parser.add_argument(
        "--image-subset",
        help="Only consider images that are in the results file",
        action="store_true")
    parser.add_argument(
        "--eval-file",
        default='eval.json',
        type=str,
        help="Evaluation results file")
    parser.add_argument(
        "--eval-images-file",
        default='eval-images.json',
        type=str,
        help="Evaluation images results file")
    args = vars(parser.parse_args(args))
    evaluate_captions(
        annotation_file=args['annotation-file'],
        results_file=args['results-file'],
        eval_file=args['eval_file'],
        eval_images_file=args['eval_images_file'])


if __name__ == '__main__':
    #main()
    main([
          r'D:\Projects\data\mscoco\2017\annotations\captions_val2017.json',
        '../../visual-attention/experiments/output/model/img_ctx-nosen/v1/results-val.json'
    ])
