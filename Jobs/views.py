from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from Jobs.models import CompanyDb,JobDb,ApplicationDb
from Jobs.serializers import Comapny_serializer,Job_serializer,Application_serializer

# Create your views here.

class CompanyCreateListView(APIView):
    def get(self,request):
        qs=CompanyDb.objects.all()
        serializer_instance=Comapny_serializer(qs,many=True)
        return Response(data=serializer_instance.data)
    def post(self,request):
        form_data=request.data
        serializer_instance=Comapny_serializer(data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

class CompanyRetrieveUpdateDelete(APIView):
    def get(self,request,pk):
        qs=get_object_or_404(CompanyDb,id=pk)
        serializer_instance=Comapny_serializer(qs)
        return Response(data=serializer_instance.data)
    def put(self,request,pk):
        form_data=request.data
        company_object=get_object_or_404(CompanyDb,id=pk)
        serializer_instance=Comapny_serializer(data=form_data,instance=company_object)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)
    def delete(self,request,pk):
        company_object=get_object_or_404(CompanyDb,id=pk)
        company_object.delete()
        return Response(data={
            "Message":"Data Deleted Successfully....."
        })

class JobCreateListView(APIView):

    def get(self, request):
        qs = JobDb.objects.all()
        serializer_instance = Job_serializer(qs, many=True)
        return Response(data=serializer_instance.data)

    def post(self, request):
        serializer_instance = Job_serializer(data=request.data)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(
                data=serializer_instance.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            data=serializer_instance.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class JobRetrieveUpdateDelete(APIView):

    def get(self, request, pk):
        job_object = get_object_or_404(JobDb, id=pk)
        serializer_instance = Job_serializer(job_object)
        return Response(data=serializer_instance.data)

    def put(self, request, pk):
        job_object = get_object_or_404(JobDb, id=pk)

        serializer_instance = Job_serializer(
            instance=job_object,
            data=request.data
        )

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)

        return Response(
            data=serializer_instance.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        job_object = get_object_or_404(JobDb, id=pk)
        job_object.delete()
        return Response({"Message": "Job Deleted Successfully"})


class ApplicationCreateListView(APIView):

    def get(self, request):
        qs = ApplicationDb.objects.all()
        serializer_instance = Application_serializer(qs, many=True)
        return Response(data=serializer_instance.data)

    def post(self, request):
        serializer_instance = Application_serializer(data=request.data)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(
                data=serializer_instance.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            data=serializer_instance.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class ApplicationRetrieveUpdateDelete(APIView):

    def get(self, request, pk):
        application_object = get_object_or_404(ApplicationDb, id=pk)
        serializer_instance = Application_serializer(application_object)
        return Response(data=serializer_instance.data)

    def put(self, request, pk):
        application_object = get_object_or_404(ApplicationDb, id=pk)

        serializer_instance = Application_serializer(
            instance=application_object,
            data=request.data
        )

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data)

        return Response(
            data=serializer_instance.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        application_object = get_object_or_404(ApplicationDb, id=pk)
        application_object.delete()
        return Response(
            {"Message": "Application Deleted Successfully"}
        )
