import os

import pandas as pd
import werkzeug
from flask import Flask, jsonify, request
import json
import numpy as np
import pickle
from flask_restful import Resource, Api, reqparse
from data_extraction import data_extraction_service
from data_cleaning import data_cleaning_service
from constants import Constants

app = Flask(__name__)
api = Api(app)


class DataCleaningResource(Resource):

    def post(self):

        file = request.files['file']
        file_type = file.content_type

        if file_type.split('/')[1] == 'csv':
            df = data_extraction_service.extract_from_csv(file)
        elif file_type.split('/')[0] == 'json':
            df = data_extraction_service.extract_from_json(file)
        else:
            return 'Unimplemented path'

        cleaned_df = data_cleaning_service.clean_data(df)

        return {"cleaned_df": cleaned_df.to_dict()}, 200


api.add_resource(DataCleaningResource, '/clean')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5051)
