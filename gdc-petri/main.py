#!/usr/bin/env python

import argparse
import logging
import os
import sys

import sqlalchemy
from snakes import nets

def setup_logging(tool_name, args, uuid):
    logging.basicConfig(
        filename=os.path.join(uuid + '_' + tool_name + '.log'),
        level=args.level,
        filemode='w',
        format='%(asctime)s %(levelname)s %(message)s',
        datefmt='%Y-%m-%d_%H:%M:%S_%Z',
    )
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
    logger = logging.getLogger(__name__)
    return logger

def make_net():
    gdc_net = nets.PetriNet('gdc-net')
    p_bqsr_normal_wxs_bam = nets.Place('bqsr-normal-wxs-bam') # upon placement of bam in node
    p_input_normal_bam = nets.Place('input-normal-bam') # must consume bam nodes
    p_input_normal_metadata = nets.Place('input-normal-metadata') # must consume metadata nodes
    t_dnaseq_normal_wxs_workflow = nets.Place('dnaseq-normal-wxs-workflow')
    gdc_net.add_place(p_input_normal_metadata)
    gdc_net.add_place(p_input_normal_bam)
    gdc_net.add_place(p_bqsr_normal_wxs_bam)
    gdc_net.add_transition(t_dnaseq_normal_wxs_workflow)
    gdc_net.add_input('input-normal-bam', 'dnaseq-normal-wxs-workflow')
    gdc_net.add_input('input-normal-metadata', 'dnaseq-normal-wxs-workflow')
    gdc_net.add_output('bwsr-normal-wxs-bam', 'dnaseq-normal-wxs-workflow')
    
def main():
    parser = argparse.ArgumentParser('a petri gdc')

    # Logging flags.
    parser.add_argument('-d', '--debug',
        action = 'store_const',
        const = logging.DEBUG,
        dest = 'level',
        help = 'Enable debug logging.',
    )
    parser.set_defaults(level = logging.INFO)

    
    parser.add_argument('--bam',
                        required = True
    )
    parser.add_argument('--input_state',
                        required = True
    )
    parser.add_argument('--metric_name',
                        required = True
    )
    parser.add_argument('--metric_path',
                        required = True
    )
    parser.add_argument('--uuid',
                        required = True
    )

    # setup required parameters
    args = parser.parse_args()
    bam = args.input_state
    input_state = args.input_state
    metric_name = args.metric_name
    metric_path = args.metric_path
    uuid = args.uuid

    logger = setup_logging('samtools_' + metric_name, args, uuid)

    sqlite_name = uuid + '.db'
    engine_path = 'sqlite:///' + sqlite_name
    engine = sqlalchemy.create_engine(engine_path, isolation_level='SERIALIZABLE')

    make_net()
    return

if __name__ == '__main__':
    main()
