from skill_system.skill_deployer import SkillDeployer


class SkillManager():
    def __init__(self):
        self.__deployer = SkillDeployer()

    def manage(self):
        print("manage")

    def use_deployer(self):
        self.__deployer.use_helper()

