from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from projects.models import (
    Discussion,
    DiscussionReply,
    DiscussionStar,
    Project,
    ProjectMember,
    ProjectRequest,
)
from projects.serializers import (
    DiscussionReplySerializer02,
    DiscussionStarSerializer02,
    FieldSerializer01,
    ProjectRequestSerializer01,
    ProjectSerializer01,
    ProjectSerializer03,
)
from rest_framework import status

from ..models import Profile, Skill
from ..serializers import (
    ProfileSerializer01,
    ProfileSerializer02,
    ProfileSerializer03,
    SkillSerializer01,
)

User = get_user_model()
client = Client()
BASE_URL = "/api/profiles/"


class TestSignupView(TestCase):
    pass


class TestEditMyProfileView(TestCase):
    pass


class TestGetMyProfile(TestCase):
    url = BASE_URL + "get-my-profile"

    def setUp(self):
        self.user = User.objects.create(username="jeff")

    def test_req(self):
        response = client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        client.force_login(self.user)
        response = client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for method in ["delete", "put", "patch", "post"]:
            response = getattr(client, method)(self.url)
            self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_res(self):
        serializer = ProfileSerializer01(self.user.profile)

        client.force_login(self.user)
        response = client.get(self.url)
        self.assertEqual(response.data, serializer.data)


class TestGetProfile(TestCase):
    url = BASE_URL + "get-profile/"

    def setUp(self):
        self.user = User.objects.create(username="jeff")

    def test_req(self):
        response = client.get(f"{self.url}{self.user.username}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for method in ["delete", "put", "patch", "post"]:
            response = getattr(client, method)(self.url + self.user.username)
            self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_res(self):
        serializer = ProfileSerializer01(self.user.profile)

        response = client.get(self.url + "unexistent-username")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, "Usuário não encontrado")

        response = client.get(self.url + self.user.username)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)


class TestGetProfileProjects(TestCase):
    url = BASE_URL + "get-profile-projects/"

    def setUp(self):
        self.user = User.objects.create(username="jeff")

    def test_req(self):
        response = client.get(self.url + self.user.username)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for method in ["delete", "put", "patch", "post"]:
            response = getattr(client, method)(self.url + self.user.username)
            self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_res(self):
        response = client.get(self.url + "unexistent-username")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, "Usuário não encontrado")

        project01 = Project.objects.create(name="SpaceX", category="startup", slogan="Wait for us, red planet!")
        project02 = Project.objects.create(name="BlueOrigin", category="startup", slogan="Your favorite space company")
        ProjectMember.objects.create(profile=self.user.profile, project=project01, role="admin")
        ProjectMember.objects.create(profile=self.user.profile, project=project02, role="member")
        serializer = ProjectSerializer01([project01, project02], many=True)

        response = client.get(self.url + self.user.username)
        self.assertEqual(response.data, serializer.data)


class TestGetFilteredProfiles(TestCase):
    url = BASE_URL + "get-filtered-profiles/"

    def test_req(self):
        response = client.get(self.url + "")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = client.get(self.url + "fel")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for method in ["delete", "put", "patch", "post"]:
            response = getattr(client, method)(self.url + "feli")
            self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_res(self):
        User.objects.create(username="michael.JJ")
        User.objects.create(username="veronica")
        User.objects.create(username="jordan")
        User.objects.create(username="joanne")

        query = "j"
        response = client.get(self.url + query)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(
            response.data, ProfileSerializer03(Profile.objects.filter(user__username__icontains=query), many=True).data
        )

        query = "JO"
        response = client.get(self.url + query)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(
            response.data, ProfileSerializer03(Profile.objects.filter(user__username__icontains=query), many=True).data
        )

        query = "joanne"
        response = client.get(self.url + query)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(
            response.data, ProfileSerializer03(Profile.objects.filter(user__username__icontains=query), many=True).data
        )

        query = "unexistent-username"
        response = client.get(self.url + query)
        self.assertEqual(len(response.data), 0)
        self.assertEqual(
            response.data, ProfileSerializer03(Profile.objects.filter(user__username__icontains=query), many=True).data
        )


class TestGetProfileList(TestCase):
    url = BASE_URL + "get-profile-list"

    def test_req(self):
        response = client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for method in ["delete", "put", "patch", "post"]:
            response = getattr(client, method)(self.url)
            self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_res(self):
        # asserting that the superuser's profile won't be returned by the view
        superuser = User.objects.create(username="superuser", is_superuser=True)
        profiles = [superuser.profile]

        for i in range(20):
            user = User.objects.create(username=f"user0{i}")
            profiles.append(user.profile)

        response = client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, ProfileSerializer03(profiles[1:21], many=True).data)


class TestGetSkillsNameList(TestCase):
    url = BASE_URL + "get-skills-name-list"

    def test_req(self):
        response = client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for method in ["delete", "put", "patch", "post"]:
            response = getattr(client, method)(self.url)
            self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_res(self):
        skill01 = Skill.objects.create(name="design")
        skill02 = Skill.objects.create(name="physics")
        skill03 = Skill.objects.create(name="programming")

        skills = [skill01, skill02, skill03]

        response = client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, SkillSerializer01(skills, many=True).data)


# ----- CONTINUE FROM HERE --------------------


class TestGetNotifications(TestCase):
    url = BASE_URL + "get-notifications"

    def test_req(self):
        response = client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        for method in ["delete", "put", "patch", "post"]:
            response = getattr(client, method)(self.url)
            self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_res(self):
        user = User.objects.create(username="felipe")
        client.force_login(user)

        profile01 = User.objects.create(username="peter").profile
        profile02 = User.objects.create(username="jane").profile

        project01 = Project.objects.create()
        project02 = Project.objects.create()
        project03 = Project.objects.create()

        discussion01 = Discussion.objects.create(profile=user.profile, project=project01)
        discussion02 = Discussion.objects.create(profile=user.profile, project=project02)

        project_request01 = ProjectRequest.objects.create(project=project01, profile=profile01, type="invitation")
        project_request02 = ProjectRequest.objects.create(project=project01, profile=profile02, type="entry_request")

        response = client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, "Dados inválidos!")

        response = client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data,
            {
                "projects_invitations": [],
                "projects_entering_requests": [],
                "discussions_stars": [],
                "discussions_replies": [],
            },
        )

        project01.students.add(student)
        project01.save()

        project02.pending_invited_students.add(student)
        project02.save()
        project03.pending_invited_students.add(student)
        project03.save()

        discussion_star01 = DiscussionStar.objects.create(discussion=discussion01, profile=profile01)
        discussion_star02 = DiscussionStar.objects.create(discussion=discussion01, profile=profile02)
        discussion_star03 = DiscussionStar.objects.create(discussion=discussion02, profile=profile01)

        discussion_reply01 = DiscussionReply.objects.create(discussion=discussion01, profile=profile01)
        discussion_reply02 = DiscussionReply.objects.create(discussion=discussion01, profile=profile02)
        discussion_reply03 = DiscussionReply.objects.create(discussion=discussion02, profile=profile01)

        response = client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data,
            {
                "projects_invitations": ProjectSerializer03([project03, project02], many=True).data,
                "projects_entering_requests": ProjectRequestSerializer01(
                    [project_entering_request02, project_entering_request01], many=True
                ).data,
                "discussions_stars": DiscussionStarSerializer02(
                    [discussion_star03, discussion_star02, discussion_star01], many=True
                ).data,
                "discussions_replies": DiscussionReplySerializer02(
                    [discussion_reply03, discussion_reply02, discussion_reply01], many=True
                ).data,
            },
        )

        student.delete()
        mentor = Mentor.objects.create(profile=user.profile)

        response = client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data,
            {
                "projects_invitations": [],
                "projects_entering_requests": [],
                "discussions_stars": DiscussionStarSerializer02(
                    [discussion_star03, discussion_star02, discussion_star01], many=True
                ).data,
                "discussions_replies": DiscussionReplySerializer02(
                    [discussion_reply03, discussion_reply02, discussion_reply01], many=True
                ).data,
            },
        )

        project01.mentors.add(mentor)
        project02.pending_invited_mentors.add(mentor)
        project02.save()
        project03.pending_invited_mentors.add(mentor)
        project03.save()

        response = client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data,
            {
                "projects_invitations": ProjectSerializer03([project03, project02], many=True).data,
                "projects_entering_requests": [],
                "discussions_stars": DiscussionStarSerializer02(
                    [discussion_star03, discussion_star02, discussion_star01], many=True
                ).data,
                "discussions_replies": DiscussionReplySerializer02(
                    [discussion_reply03, discussion_reply02, discussion_reply01], many=True
                ).data,
            },
        )


class TestGetNotificationsNumber(TestCase):
    url = BASE_URL + "get-notifications-number"

    def test_req(self):
        response = client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        for method in ["delete", "post", "put", "patch"]:
            response = getattr(client, method)(self.url)
            self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_res(self):
        user = User.objects.create()
        client.force_login(user)

        response = client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, "Dados inválidos!")

        student = Student.objects.create(profile=user.profile)

        response = client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, 0)

        project01 = Project.objects.create()
        project01.pending_invited_students.add(student)  # 1
        project01.save()

        project02 = Project.objects.create()
        project02.students.add(student)
        project02.save()

        ProjectRequest.objects.create(project=project02)  # 2

        discussion = Discussion.objects.create(profile=user.profile)
        DiscussionStar.objects.create(discussion=discussion)  # 3
        DiscussionStar.objects.create(discussion=discussion)  # 4
        DiscussionReply.objects.create(discussion=discussion)  # 5
        DiscussionReply.objects.create(discussion=discussion)  # 6

        response = client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, 6)

        student.delete()

        mentor = Mentor.objects.create(profile=user.profile)

        project01.pending_invited_mentors.add(mentor)
        project01.save()

        project02.mentors.add(mentor)
        project02.save()

        response = client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, 5)


class TestVisualizeNotifications(TestCase):
    url = BASE_URL + "visualize-notifications"

    def test_req(self):
        response = client.patch(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        for method in ["get", "delete", "post", "put"]:
            response = getattr(client, method)(self.url)
            self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_res(self):
        user = User.objects.create()
        client.force_login(user)

        response = client.patch(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, "success")

        discussion = Discussion.objects.create(profile=user.profile)
        discussion_star01 = DiscussionStar.objects.create(discussion=discussion)
        discussion_star02 = DiscussionStar.objects.create(discussion=discussion)

        discussion_reply01 = DiscussionReply.objects.create(discussion=discussion)
        discussion_reply02 = DiscussionReply.objects.create(discussion=discussion)

        self.assertFalse(discussion_star01.visualized)
        self.assertFalse(discussion_star02.visualized)

        self.assertFalse(discussion_reply01.visualized)
        self.assertFalse(discussion_reply02.visualized)

        response = client.patch(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, "success")

        discussion_star01.refresh_from_db()
        discussion_star02.refresh_from_db()

        discussion_reply01.refresh_from_db()
        discussion_reply02.refresh_from_db()

        self.assertTrue(discussion_star01.visualized)
        self.assertTrue(discussion_star02.visualized)

        self.assertTrue(discussion_reply01.visualized)
        self.assertTrue(discussion_reply02.visualized)
