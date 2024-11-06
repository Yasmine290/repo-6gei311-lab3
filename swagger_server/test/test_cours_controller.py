# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestCoursController(BaseTestCase):
    """CoursController integration test stubs"""

    def test_courses_course_id_delete(self):
        """Test case for courses_course_id_delete

        Supprimer un cours
        """
        response = self.client.open(
            '/courses/{courseId}'.format(courseId=None),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_courses_course_id_get(self):
        """Test case for courses_course_id_get

        Obtenir un cours spécifique
        """
        response = self.client.open(
            '/courses/{courseId}'.format(courseId=None),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_courses_course_id_put(self):
        """Test case for courses_course_id_put

        Mettre à jour un cours
        """
        response = self.client.open(
            '/courses/{courseId}'.format(courseId=None),
            method='PUT')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_courses_get(self):
        """Test case for courses_get

        Obtenir la liste des cours
        """
        response = self.client.open(
            '/courses',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_courses_post(self):
        """Test case for courses_post

        Créer un nouveau cours
        """
        response = self.client.open(
            '/courses',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
