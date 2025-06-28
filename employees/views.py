from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Manager, Intern

class StaffRoleView(APIView):
    def get(self, request):
        managers = Manager.objects.all()
        interns = Intern.objects.all()

        data = []

        for manager in managers:
            data.append({
                'id': manager.id,
                'name': f"{manager.first_name} {manager.last_name}",
                'role': manager.get_role()
            })

        for intern in interns:
            data.append({
                'id': intern.id,
                'name': f"{intern.first_name} {intern.last_name}",
                'role': intern.get_role()
            })

        return Response(data)
