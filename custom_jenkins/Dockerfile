FROM jenkins/jenkins:lts

USER root

# Install prerequisites
RUN apt-get update -y && \
    apt-get install -y ca-certificates curl gnupg lsb-release sudo && \
    curl -fsSL https://get.docker.com -o get-docker.sh && \
    sh get-docker.sh && \
    rm get-docker.sh && \
    apt-get clean

# Add Jenkins to docker group
RUN groupadd -f docker && \
    usermod -aG docker jenkins

# Create Docker volume
RUN mkdir -p /var/lib/docker
VOLUME /var/lib/docker

USER jenkins
