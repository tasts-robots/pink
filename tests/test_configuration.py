#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2022 Stéphane Caron
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Test the Configuration type.
"""

import unittest

import jvrc_description
import numpy as np

import pink
from pink.exceptions import NotWithinConfigurationLimits
from pink.models import build_from_urdf


class TestConfiguration(unittest.TestCase):
    def test_assume_configuration(self):
        """
        Assuming a configuration does not change data.
        """
        robot = build_from_urdf(jvrc_description.urdf_path)
        robot.data.J.fill(42.0)
        configuration = pink.assume_configuration(robot, robot.q0)
        self.assertTrue(np.allclose(configuration.data.J, 42.0))

    def test_apply_configuration(self):
        """
        Applying a configuration computes Jacobians.
        """
        robot = build_from_urdf(jvrc_description.urdf_path)
        robot.data.J.fill(42.0)
        configuration = pink.apply_configuration(robot, robot.q0)
        J_check = np.array(
            [
                [
                    1.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.096,
                    0.389,
                    0.0,
                    0.746,
                    -0.0,
                    -0.0,
                    -0.096,
                    0.389,
                    0.0,
                    0.746,
                    0.0,
                    -0.192,
                    0.0,
                    -0.522,
                    0.0,
                    0.24,
                    -0.217,
                    0.24,
                    0.0,
                    0.24,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    -0.645,
                    -0.522,
                    -0.0,
                    -0.24,
                    -0.217,
                    -0.24,
                    0.0,
                    -0.24,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                ],
                [
                    0.0,
                    1.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    -0.746,
                    -0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    -0.746,
                    -0.0,
                    0.0,
                    0.0,
                    0.192,
                    0.0,
                    0.522,
                    0.0,
                    0.0,
                    -0.0,
                    -0.022,
                    -0.0,
                    -0.124,
                    -0.169,
                    -0.124,
                    -0.169,
                    -0.106,
                    -0.151,
                    0.003,
                    0.645,
                    0.0,
                    0.0,
                    0.522,
                    0.0,
                    0.0,
                    -0.0,
                    -0.022,
                    -0.0,
                    -0.124,
                    -0.169,
                    -0.124,
                    -0.169,
                    -0.106,
                    -0.151,
                ],
                [
                    0.0,
                    0.0,
                    1.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    -0.096,
                    0.0,
                    -0.02,
                    -0.096,
                    0.02,
                    0.0,
                    0.096,
                    0.0,
                    -0.02,
                    0.096,
                    0.02,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    -0.24,
                    0.0,
                    0.004,
                    0.0,
                    -0.24,
                    0.0,
                    -0.246,
                    -0.246,
                    -0.246,
                    -0.246,
                    -0.217,
                    -0.217,
                    -0.0,
                    -0.0,
                    -0.003,
                    0.0,
                    0.24,
                    0.0,
                    0.004,
                    0.0,
                    0.24,
                    0.0,
                    0.246,
                    0.246,
                    0.246,
                    0.246,
                    0.217,
                    0.217,
                ],
                [
                    0.0,
                    0.0,
                    0.0,
                    1.0,
                    0.0,
                    0.0,
                    0.0,
                    1.0,
                    0.0,
                    0.0,
                    1.0,
                    0.0,
                    0.0,
                    1.0,
                    0.0,
                    0.0,
                    1.0,
                    0.0,
                    0.0,
                    0.0,
                    1.0,
                    0.0,
                    1.0,
                    0.0,
                    0.0,
                    0.0,
                    1.0,
                    0.0,
                    1.0,
                    1.0,
                    1.0,
                    1.0,
                    1.0,
                    1.0,
                    0.0,
                    1.0,
                    0.0,
                    0.0,
                    1.0,
                    0.0,
                    0.0,
                    0.0,
                    1.0,
                    0.0,
                    1.0,
                    1.0,
                    1.0,
                    1.0,
                    1.0,
                    1.0,
                ],
                [
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    1.0,
                    0.0,
                    1.0,
                    0.0,
                    0.0,
                    1.0,
                    0.0,
                    1.0,
                    1.0,
                    0.0,
                    0.0,
                    1.0,
                    0.0,
                    1.0,
                    0.0,
                    1.0,
                    0.0,
                    1.0,
                    0.0,
                    0.0,
                    1.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    1.0,
                    1.0,
                    0.0,
                    0.0,
                    1.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                ],
                [
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    1.0,
                    0.0,
                    0.0,
                    1.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    1.0,
                    0.0,
                    0.0,
                    0.0,
                    1.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    1.0,
                    0.0,
                    1.0,
                    0.0,
                    1.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    1.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    1.0,
                    0.0,
                    1.0,
                    0.0,
                    1.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                ],
            ]
        )
        self.assertTrue(np.allclose(configuration.data.J, J_check))

    def test_transform_found(self):
        """
        Return the pose of an existing robot body.
        """
        robot = build_from_urdf(jvrc_description.urdf_path)
        configuration = pink.apply_configuration(robot, robot.q0)
        transform_pelvis_to_world = configuration.get_transform_body_to_world(
            "PELVIS_S"
        )
        self.assertTrue(
            np.allclose(
                transform_pelvis_to_world.np[3, :],
                np.array([0.0, 0.0, 0.0, 1.0]),
            )
        )

    def test_transform_not_found(self):
        """
        Raise an error when the request robot body is not found.
        """
        robot = build_from_urdf(jvrc_description.urdf_path)
        configuration = pink.apply_configuration(robot, robot.q0)
        with self.assertRaises(KeyError):
            configuration.get_transform_body_to_world("foo")

    def test_check_limits(self):
        """
        Raise an error if and only if a joint limit is exceened.
        """
        robot = build_from_urdf(jvrc_description.urdf_path)
        q = robot.q0
        configuration = pink.apply_configuration(robot, q)
        configuration.check_limits()
        q[-10] += 1e4  # move configuration out of bounds
        configuration = pink.apply_configuration(robot, q)
        with self.assertRaises(NotWithinConfigurationLimits):
            configuration.check_limits()

    def test_q_is_a_read_only_copy(self):
        """
        The `q` attribute of a configuration is a read-only copy.
        """
        robot = build_from_urdf(jvrc_description.urdf_path)
        original_q = robot.q0
        configuration = pink.apply_configuration(robot, original_q)
        the_answer = 42.0
        self.assertNotEqual(configuration.q[2], the_answer)
        original_q[2] = the_answer
        self.assertNotEqual(configuration.q[2], the_answer)
        with self.assertRaises(ValueError):
            configuration.q[2] += 3.0  # read-only

    def test_tangent_eye(self):
        """
        Configuration's tangent eye is an identity matrix.
        """
        robot = build_from_urdf(jvrc_description.urdf_path)
        configuration = pink.apply_configuration(robot, robot.q0)
        v = np.array([i for i in range(robot.model.nv)])
        self.assertTrue(np.allclose(configuration.tangent.eye.dot(v), v))

    def test_tangent_ones(self):
        """
        Configuration's tangent ones is a vector of 1.0's.
        """
        robot = build_from_urdf(jvrc_description.urdf_path)
        configuration = pink.apply_configuration(robot, robot.q0)
        self.assertEqual(np.sum(configuration.tangent.ones), robot.model.nv)

    def test_tangent_zeros(self):
        """
        Configuration's tangent ones is a vector of 0.0's.
        """
        robot = build_from_urdf(jvrc_description.urdf_path)
        configuration = pink.apply_configuration(robot, robot.q0)
        self.assertAlmostEqual(np.sum(configuration.tangent.zeros), 0.0)
        self.assertEqual(len(configuration.tangent.zeros), robot.model.nv)
